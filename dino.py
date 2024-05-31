import pygame

class Dino:
	def __init__(self):
		self.image = pygame.image.load("Graphics/dino.png")
		self.position = pygame.Vector2(100, 100)
		self.speed = 10

	def draw(self, window):
		window.blit(self.image, (self.position.x, self.position.y))

	def update(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]:
			self.position.x += self.speed
		if keys[pygame.K_LEFT]:
			self.position.x -= self.speed
		if keys[pygame.K_UP]:
			self.position.y -= self.speed
		if keys[pygame.K_DOWN]:
			self.position.y += self.speed

	def get_rect(self):
		return self.image.get_rect(topleft = (self.position.x, self.position.y))

	def draw_hitbox(self, window, is_colliding):
		if is_colliding:
		 pygame.draw.rect(window, 'red', self.get_rect(), 3)