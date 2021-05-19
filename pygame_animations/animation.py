# pygame instance
import pygame as _pg

# load effects
from .effects import Effects
from .events import _anim_started, _anim_stopped

# all running animations
# please dont modify it yourself
_running = []

class Animation:
	"""An animation.

Parameters:
    target
        the object which will be animated. It can be anything.
    duration (int/float)
        the duration of the animation, in seconds.
    effect (callable)
        the effect to apply to the animation. It can be a built-in effect (see pygame_animations.Effects) or any function that takes one float parameter and return a float
    flags
        a string with flags separated by commas, used to identify the animation.
    **attrs
        the attributes of the target to animate. To animate `a.b`, use `a__b`.

Attributes:
    target
        the object that will be animated.
    duration (int)
        the duration of the animation, in milliseconds.

Example : move a sprite to x=100 in 1 second
    myanimation = Animation(mysprite, 1, rect__x=100)
or
    myanimation = Animation(mysprite.rect, 1, x=100)"""
	def __init__(self, target, duration, effect=Effects.linear, /, flags=None, **attrs):
		self._end = attrs
		self._start = None
		self._startticks = 0
		self.duration = round(duration*1000)
		self.target = target
		self._setflags(flags)
		self._effect = effect
		
	def __repr__(self):
		return f'Animation(target={repr(self.target)}, duration={self.duration}, effect={self._effect})'

	# lock object after initialisation
	def __setattr__(self, attr, val):
		if hasattr(self, '_effect') and not attr in ('_start', '_startticks'):
			raise TypeError('Animations can\'t be modified after initialisation')
		else:
			object.__setattr__(self, attr, val)

	def __delattr__(self, attr):
		if hasattr(self, '_effect'):
			raise TypeError('Animations can\'t be modified after initialisation')
		else:
			object.__delattr__(self, attr, val)

	def __add__(self, obj):
		if issubclass(type(obj), Animation):
			return AnimationSequence(self, obj)
		return NotImplemented

	def __and__(self, obj):
		if issubclass(type(obj), Animation):
			return AnimationGroup(self, obj)
		return NotImplemented
		
	def start(self):
		"""Run the animation. It can only be used once."""
		if self._start is not None:
			raise RuntimeError('Animations can only be run once')
		# initial state of all attributes
		self._start = dict()	
		for attr in self._end:
			sep = attr.split('__')
			subtarget, subattr = eval('.'.join(['self.target']+sep[:-1])), sep[-1]
			self._start[attr] = getattr(subtarget, subattr)
		# start time
		if not self._startticks:
			self._startticks = _pg.time.get_ticks()
		# get updated
		_running.append(self)
		_anim_started(self)
		
	def stop(self, /, noerror=False):
		"""Stop the animation and leave the target as it is. Once stoppped, it cannot be resumed.

    noerror (optional): when calling this method on an animation that isn't running, a RuntimeError will be raised if set to False, and just ignored it if set to True"""
		if not self in _running:
			if noerror: return
			raise RuntimeError('Not running')
		_running.remove(self)
		_anim_stopped(self)

	def cancel(self, /, noerror=False):
		"""like Animation.stop(), but reset the target in its initial state."""
		if not self in _running:
			if noerror: return
			raise RuntimeError('Not running')
		_running.remove(self)
		_anim_stopped(self)
		for attr in self._start:
			sep = attr.split('__')
			subtarget, subattr = eval('.'.join(['self.target']+sep[:-1])), sep[-1]
			setattr(subtarget, subattr, self._start[attr])

	def fastforward(self, /, noerror=False):
		"""like Animation.stop(), but set the target in its final state."""
		if not self in _running:
			if noerror: return
			raise RuntimeError('Not running')
		_running.remove(self)
		_anim_stopped(self)
		for attr in self._end:
			sep = attr.split('__')
			subtarget, subattr = eval('.'.join(['self.target']+sep[:-1])), sep[-1]
			setattr(subtarget, subattr, self._end[attr])
		
	def is_running(self):
		"""Return True if the animation is running."""
		return self in _running
		
	def can_run(self):
		"""Return True if the animation hasn't been arleady started."""
		return self._start is None

	def match(self, flags):
		"""return true if the animation's flags match the given flags.

flags must be a string, with flags separated by commas.
special flags:
"*" will match anyhing
"flag1|flag2" will match either flag1 or flag2

for example, "flag1,flag2|flag3" will match "flag1,flag2" or "flag1,flag3" 

an animation without flags will not match anything"""
		flags = flags.split(',')
		if len(self._flags) != len(flags):
			return False
		for i, f in enumerate(flags):
			if f == '*':
				continue
			for f in r.split('|'):
				if not f.isalnum():
					raise ValueError(f'invalid flag "{f}" : flags must be alphanumeric')
				if f == self._flags[i]:
					break
			else:
				return False
		return True

	def _setflags(self, farg):
		self._flags = tuple()
		if flags is not None:
			for f in flags.split(','):
				if not f.isalnum():
					raise ValueError(f'invalid flag "{f}" : flags must be alphanumeric')
				if f in self._flags:
					raise ValueError(f'duplicated flag "{f}"')
				self._flags += (f,)
	
	def _update(self, ticks):
		# time since start
		dt = ticks - self._startticks
		# progression in time 
		x = dt/self.duration
		# progression of the animation
		y = self._effect(min(max(x, 0), 1))
		for attr in self._start:
			sep = attr.split('__')
			subtarget, subattr = eval('.'.join(['self.target']+sep[:-1])), sep[-1]
			initial, final = self._start[attr], self._end[attr]
			# map y between initial and final
			setattr(subtarget, subattr, initial+y*(final-initial))
		# if finished
		if x > 1:
			_running.remove(self)
			_anim_stopped(self)


class AnimationSequence (Animation):
	"""Multiple animations played one after another.
You can create AnimationSequences by adding multiple animations together : anim1 + anim2 is the same as AnimationSequence(anim1, anim2)

Parameters:
    a, b, *others
        animations for the sequence.
    flag
        a string with flags separated by commas, used to identify the animation.

Attributes:
    animations
        a tuple of the animations that makes up the sequence, in order. There is at least 2 animations.
    duration (int)
        the duration of the animation, in milliseconds. it is the sum of the durations of all the `animations`."""
	def __init__(self, a, b, *others, flags=None):
		self.animations = tuple()
		for anim in (a, b)+others:
			if not anim.can_run():
				raise RuntimeError(f'the animation <{repr(anim)}> has arleady been started.')
			if type(a) is AnimationSequence:
				self.animations += anim.animations
			else:
				self.animations += (anim,)
		self._startticks = 0
		self._start = None
		self.duration = sum([anim.duration for anim in self.animations])
		self._setflags(flags)
		self._effect = None
		
	def __repr__(self):
		return f'AnimationSequence[{", ".join([repr(anim) for anim in self.animations])}]'
		
	def start(self):
		"""Run the animation. It can only be used once."""
		if self._start is not None:
			raise RuntimeError('Animations can only be run once')
		self._start = 1	
		# start time
		startticks = self._startticks if self.startticks else _pg.time.get_ticks()
		for anim in self.animations:
			anim._startticks = startticks
			anim.start()
			startticks += anim.duration
		# get updated
		_running.append(self)
		_anim_started(self)
		
	def stop(self, /, noerror=False):
		"""Stop itself and call stop() on the animations. Once stoppped, it cannot be resumed.

    noerror (optional): when calling this method on an animation that isn't running, a RuntimeError will be raised if set to False, and just ignored it if set to True"""
		if not self in _running:
			if noerror: return
			raise RuntimeError('Not running')
		for anim in self.animations:
			anim.stop(noerror=True)
		_running.remove(self)
		_anim_stopped(self)

	def cancel(self, /, noerror=False):
		"""like AnimationSequence.stop(), but call cancel() on the animations."""
		if not self in _running:
			if noerror: return
			raise RuntimeError('Not running')
		for anim in self.animations:
			anim.cancel(noerror=True)
		_running.remove(self)
		_anim_stopped(self)

	def fastforward(self, /, noerror=False):
		"""like AnimationSequence.stop(), but call fastforward() on the animations."""
		if not self in _running:
			if noerror: return
			raise RuntimeError('Not running')
		for anim in self.animations:
			anim.fastforward(noerror=True)
		_running.remove(self)
		_anim_stopped(self)
	
	def _update(self, ticks):
		if all([not anim.is_running() for anim in self.animations]):
			_running.remove(self)
			_anim_stopped(self)


class AnimationGroup (Animation):
	"""Multiple animations played at the same time.
You can create AnimationGroups by and-ing multiple animations together : anim1 & anim2 is the same as AnimationGroup(anim1, anim2)

Parameters:
    a, b, *others
        animations for the sequence.
    flag
        a string with flags separated by commas, used to identify the animation.

Attributes:
    animations
        a tuple of the animations that makes up the sequence. There is at least 2 animations.
    duration (int)
        the duration of the animation, in milliseconds. it is the longest duration in all of the `animations`."""
	def __init__(self, a, b, *others, flags=None):
		self.animations = tuple()
		for anim in (a, b)+others:
			if not anim.can_run():
				raise RuntimeError(f'the animation <{repr(anim)}> has arleady been started.')
			if type(a) is AnimationGroup:
				self.animations += anim.animations
			else:
				self.animations += (anim,)
		self._start = None
		self.duration = max([anim.duration for anim in self.animations])
		self._setflags(flags)
		self._effect = None
		
	def __repr__(self):
		return f'AnimationGroup[{", ".join([repr(anim) for anim in self.animations])}]'
		
	def start(self):
		"""Run the animation. It can only be used once."""
		if self._start is not None:
			raise RuntimeError('Animations can only be run once')
		self._start = 1	
		# start time
		if not self._startticks:
			self._startticks = _pg.time.get_ticks()
		for anim in self.animations:
			anim._startticks = self._startticks
			anim.start()
		# get updated
		_running.append(self)
		_anim_started(self)
		
	def stop(self, /, noerror=False):
		"""Stop itself and call stop() on the animations. Once stoppped, it cannot be resumed.

    noerror (optional): when calling this method on an animation that isn't running, a RuntimeError will be raised if set to False, and just ignored it if set to True"""
		if not self in _running:
			if noerror: return
			raise RuntimeError('Not running')
		for anim in self.animations:
			anim.stop(noerror=True)
		_running.remove(self)
		_anim_stopped(self)

	def cancel(self, /, noerror=False):
		"""like AnimationGroup.stop(), but call cancel() on the animations."""
		if not self in _running:
			if noerror: return
			raise RuntimeError('Not running')
		for anim in self.animations:
			anim.cancel(noerror=True)
		_running.remove(self)
		_anim_stopped(self)

	def fastforward(self, /, noerror=False):
		"""like AnimationGroup.stop(), but call fastforward() on the animations."""
		if not self in _running:
			if noerror: return
			raise RuntimeError('Not running')
		for anim in self.animations:
			anim.fastforward(noerror=True)
		_running.remove(self)
		_anim_stopped(self)
	
	def _update(self, ticks):
		if all([not anim.is_running() for anim in self.animations]):
			_running.remove(self)
			_anim_stopped(self)