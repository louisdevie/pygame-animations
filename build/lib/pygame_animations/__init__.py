from .animation import Animation, AnimationSequence, AnimationGroup, _running, _pg
from .effects import Effects
from .events import ANIMATIONSTARTED, ANIMATIONENDED

def update_animations():
	"""update all running animations.
you need to call it before rendering each frame."""
	t = _pg.time.get_ticks()
	for a in _running:
		a._update(t)
	
def stop_all():
	"""stop all running animations. see pygame_animation.Animation.stop for more information."""
	while _running:
		_running[0].stop(noerror=True)

def cancel_all():
	"""cancel all running animations. see pygame_animation.Animation.cancel for more information."""
	while _running:
		_running[0].cancel(noerror=True)

def fastforward_all():
	"""fast-forward all running animations. see pygame_animation.Animation.fastforward for more information."""
	while _running:
		_running[0].fastforward(noerror=True)
	
__all__ = ['Animation', 'AnimationSequence', 'AnimationGroup', 'Effects', 'update_animations', 'stop_all', 'cancel_all', 'fastforward_all', 'ANIMATIONSTARTED', 'ANIMATIONENDED']
__doc__ = """implements animations for pygame

This package is an extension for pygame that lets you animate almost anything."""