import pygame

class Score:
    def __init__(self, x, y, font_size=30):
        self.score = 0
        self.font = pygame.font.SysFont(None, font_size)
        self.x = x
        self.y = y

    def increase(self, points=10):
        self.score += points

    def draw(self, screen):
        score_surf = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_surf, (self.x, self.y))
