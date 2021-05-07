import math

# all effects functions
_linear = lambda x: x
_sini = lambda x: math.sin((x-1)*(math.pi/2))+1
_sino = lambda x: math.sin(x*(math.pi/2))
_sinio = lambda x: (math.sin((x-.5)*math.pi)+1)/2
_sinshk = lambda x: math.sin(10*x*math.pi)*(1-x)
_sqro = lambda x: 1-math.pow(1-x, 2)
_sqri = lambda x: math.pow(x, 2)
_sqrio = lambda x: math.pow(x*2, 2)/2 if x<.5 else 1-math.pow(2-x*2, 2)/2
_cubeo = lambda x: 1-math.pow(1-x, 3)
_cubei = lambda x: math.pow(x, 3)
_cubeio = lambda x: math.pow(x*2, 3)/2 if x<.5 else 1-math.pow(2-x*2, 3)/2
_quado = lambda x: 1-math.pow(1-x, 4)
_quadi = lambda x: math.pow(x, 4)
_quadio = lambda x : math.pow(x*2, 4)/2 if x<.5 else 1-math.pow(2-x*2, 4)/2
_bnco = lambda x: (0.1/(x-1.17))+(1.5*x)+0.855
_bnci = lambda x: (0.1/(x+0.17))+(1.5*x)+0.590
_bncio = lambda x: -4.167*(x)*(x-0.2)*(x-1.3)

# a wrapper class to overwrite __repr__ and __str__.
class _reprwrapper:
	def __init__(self, expr, name):
		self._expr = expr
		self._name = name
	
	def __repr__(self):
		return 'pygame_animations.Effects.' + self._name
		
	def __str__(self):
		return self.__repr__()
		
	# acts as an expression
	def __call__(self, *args):
		return self._expr(*args)

# not using enum.Enum here because it doesn't work with lambdas
class _EnumEffects:
	"""Enumeration of built-in effects.

Availables effects :

    Effects.linear
        constant speed

    Effects.sin_in
    Effects.square_in
    Effects.cubic_in
    Effects.quad_in
        acceleration, from the softet to the hardest

    Effects.sin_out
    Effects.square_out
    Effects.cubic_out
    Effects.quad_out
        decceleration, from the softest to the hardest

    Effects.sin_in_out
    Effects.square_in_out
    Effects.cubic_in_out
    Effects.quad_in_out
        acceleration then decceleration, from the softest to the hardest

    Effects.sin_shake
        moves back and forth with reducing amplitude

    Effects.bounce_in
    	bounce at the start

    Effects.bounce_out
        bounce at the end

    Effects.bounce_in_out
        bounce at the start and at the end"""
	def __init__(self):
		# name each effect
		self._effects = {
			'linear': _linear,
			'sin_in': _sini,
			'sin_out': _sino,
			'sin_in_out': _sinio,
			'sin_shake': _sinshk,
			'square_in': _sqri,
			'square_out': _sqro,
			'square_in_out': _sqrio,
			'cubic_in': _cubei,
			'cubic_out': _cubeo,
			'cubic_in_out': _cubeio,
			'quad_in': _quadi,
			'quad_out': _quado,
			'quad_in_out': _quadio,
			'bounce_in': _bnci,
			'bounce_out': _bnco,
			'bounce_in_out': _bncio,
		}
		# replace each effect by a wrapper
		for name in self._effects:
			self._effects[name] = _reprwrapper(self._effects[name], name)
	
	def __repr__(self):
		return 'pygame_animations.Effects'
		
	def __str__(self):
		return self.__repr__()

	# loop through the effects
	def __iter__(self):
		return iter(self._effects.values())
	
	# get an effect by its name/index
	def __getitem__(self, key):
		if type(key) in (int, slice):
			return tuple(self._effects.values())[key]
		else:
			return self._effects[key]

	# get an effect as an attribute
	def __getattr__(self, name):
		if name.startswith('_'):
			return object.__getattr__(self, name)
		else:
			return self._effects[name]
	
	# once _effects are defined, lock the object
	def __setattr__(self, name, value):
		if hasattr(self, '_effects'):
			raise TypeError("Effects are read-only")
		else:
			object.__setattr__(self, name, value)
	
	def __delattr__(self, name):
		raise TypeError("Effects are read-only")
	
Effects = _EnumEffects()
	
__all__ = ['Effects']