import pygame

class Health:
    def __init__(self, x, y, lives=3, font_size=30):
        self.lives = lives
        self.font = pygame.font.SysFont(None, font_size)
        self.x = x
        self.y = y

    def lose_life(self):
        self.lives -= 1

    def draw(self, screen):
        health_surf = self.font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        screen.blit(health_surf, (self.x, self.y))
