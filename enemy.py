import pygame
from abc import ABC, abstractmethod

class Enemy(ABC):
    def __init__(self, x, y, speed):
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 175, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    @abstractmethod
    def move(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Alien(Enemy):
    def move(self):
        self.rect.y += self.speed

class BossAlien(Enemy):
    def __init__(self, x, y, speed, health):
        super().__init__(x, y, speed)
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))
        self.health = health

    def move(self):
        self.rect.y += self.speed

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True
        return False
