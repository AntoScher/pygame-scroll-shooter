import pygame
from bullet import Bullet

class Player:
    def __init__(self, x, y, speed, screen_width):
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.screen_width = screen_width
        self.bullets = []

    def move(self, direction):
        if direction == "LEFT" and self.rect.left > 0:
            self.rect.x -= self.speed
        elif direction == "RIGHT" and self.rect.right < self.screen_width:
            self.rect.x += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.append(bullet)

    def update_bullets(self, screen):
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
            else:
                screen.blit(bullet.image, bullet.rect)
