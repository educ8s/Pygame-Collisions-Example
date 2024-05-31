import pygame, sys
from dino import Dino

window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Pygame collisions")

clock = pygame.time.Clock()
dino = Dino()
obstacle = pygame.Rect(800, 200, 200, 175)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	dino.update()
	is_colliding = dino.get_rect().colliderect(obstacle)

	window.fill('white')
	pygame.draw.rect(window, 'black', obstacle, 5)
	dino.draw(window)
	dino.draw_hitbox(window, is_colliding)

	pygame.display.flip()
	clock.tick(60)