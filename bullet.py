import pygame

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.Surface((2, 8))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

    def move(self):
        self.rect.y -= self.speed
