# pygame instance
import pygame as _pg

# load effects
from .effects import Effects

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
	def __init__(self, target, duration, effect=Effects.linear, **attrs):
		self._end = attrs
		self._start = None
		self._startticks = 0
		self.duration = round(duration*1000)
		self.target = target
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
		self._startticks = _pg.time.get_ticks()
		# get updated
		_running.append(self)
		
	def stop(self, /, noerror=False):
		"""Stop the animation and leave the target as it is. Once stoppped, it cannot be resumed.

    noerror (optional): when calling this method on an animation that isn't running, a RuntimeError will be raised if set to False, and just ignored it if set to True"""
		if not self in _running:
			if noerror: return
			raise RuntimeError('Not running')
		_running.remove(self)

	def cancel(self, /, noerror=False):
		"""like Animation.stop(), but reset the target in its initial state."""
		if not self in _running:
			if noerror: return
			raise RuntimeError('Not running')
		_running.remove(self)
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