import pygame
import pygame_animations as anim

pygame.init()

surface = pygame.display.set_mode((640, 480))

font = pygame.font.SysFont('default', 52)

class MySprite (pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = font.render("Hello, World!", 1, (255, 255, 255))
		self.rect = self.image.get_rect()
label = MySprite()
group = pygame.sprite.Group(label)

a = anim.Animation(label, 2, anim.Effects.cubic_in_out, rect__x=640-label.rect.w)
b = anim.Animation(label, 1, anim.Effects.cubic_in_out, rect__y=480-label.rect.h)
c = a & b
print(c)

clock = pygame.time.Clock()
running = True

while running:
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			running = False

	t = pygame.time.get_ticks()
	if t>3000 and c.can_run(): # l'animation démarre après 3s
		c.start()

	anim.update_animations()

	surface.fill((0, 0, 0))
	group.draw(surface)

	pygame.display.flip()
	clock.tick(30)

pygame.quit()