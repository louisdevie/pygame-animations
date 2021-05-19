import pygame as _pg

ANIMATIONSTARTED = _pg.event.custom_type()
ANIMATIONENDED = _pg.event.custom_type()

def _anim_started(anim):
	_pg.event.post(_pg.event.Event(ANIMATIONSTARTED, animation=anim))

def _anim_stopped(anim):
	_pg.event.post(_pg.event.Event(ANIMATIONENDED, animation=anim))
