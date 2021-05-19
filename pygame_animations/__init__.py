from .animation import Animation, AnimationSequence, AnimationGroup, _running, _pg
from .effects import Effects
from .events import ANIMATIONSTARTED, ANIMATIONENDED

def update_animations():
	"""update all running animations.
you need to call it before rendering each frame."""
	t = _pg.time.get_ticks()
	for a in _running:
		a._update(t)

def _stopall(method, flags):
	if flags is None:
		dellist = _running[:]
	else:
		dellist = [a for a in _running if a.match(flags)]
	for anim in dellist:
		method(anim, noerror=True)
	
def stop_all(flags=None):
	"""stop all running animations. see pygame_animations.Animation.stop for more information.

if flags is given, stop only the animations that matches the flags. see pygame_animations.Animation.match for more information."""
	_stopall(Animation.stop, flags)

def cancel_all(flags=None):
	"""cancel all running animations. see pygame_animations.Animation.cancel for more information.

if flags is given, cancel only the animations that matches the flags. see pygame_animations.Animation.match for more information."""
	_stopall(Animation.cancel, flags)

def fastforward_all(flags=None):
	"""fast-forward all running animations. see pygame_animations.Animation.fastforward for more information.

if flags is given, fast-forward only the animations that matches the flags. see pygame_animations.Animation.match for more information."""
	_stopall(Animation.fastforward, flags)
	
__all__ = ['Animation', 'AnimationSequence', 'AnimationGroup', 'Effects', 'update_animations', 'stop_all', 'cancel_all', 'fastforward_all', 'ANIMATIONSTARTED', 'ANIMATIONENDED']
__doc__ = """implements animations for pygame

This package is an extension for pygame that lets you animate almost anything."""