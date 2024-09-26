import pygame
import random
from player import Player
from enemy import Alien, BossAlien
from score import Score
from health import Health

class Game:
    def __init__(self):
        # Настройки экрана
        self.screen_width = 400
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Space Defender")

        # Создание объектов
        self.player = Player(self.screen_width // 2, self.screen_height - 50, speed=5, screen_width=self.screen_width)
        self.enemies = []
        self.spawn_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.spawn_event, 1000)  # Спавн врагов каждую секунду

        self.score = Score(10, 10)
        self.health = Health(self.screen_width - 150, 10)

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(60)  # 60 FPS
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == self.spawn_event:
                self.spawn_enemy()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()

    def spawn_enemy(self):
        x = random.randint(50, self.screen_width - 50)
        y = -50
        speed = random.randint(2, 5)
        if random.random() < 0.1:  # 10% шанс спавна босса
            enemy = BossAlien(x, y, speed, health=30)
        else:
            enemy = Alien(x, y, speed)
        self.enemies.append(enemy)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move("LEFT")
        if keys[pygame.K_RIGHT]:
            self.player.move("RIGHT")

        # Обновление снарядов
        self.player.update_bullets(self.screen)

        # Обновление врагов
        for enemy in self.enemies[:]:
            enemy.move()
            if enemy.rect.top > self.screen_height:
                self.enemies.remove(enemy)
                self.health.lose_life()
                if self.health.lives <= 0:
                    self.running = False
            else:
                # Проверка столкновения снаряда и врага
                for bullet in self.player.bullets[:]:
                    if enemy.rect.colliderect(bullet.rect):
                        self.player.bullets.remove(bullet)
                        if isinstance(enemy, BossAlien):
                            destroyed = enemy.take_damage(10)
                            if destroyed:
                                self.enemies.remove(enemy)
                                self.score.increase(50)
                        else:
                            self.enemies.remove(enemy)
                            self.score.increase()
                        break

    def render(self):
        self.screen.fill((0, 0, 0))  # Черный фон

        # Рисование игрока
        self.screen.blit(self.player.image, self.player.rect)

        # Рисование снарядов
        for bullet in self.player.bullets:
            self.screen.blit(bullet.image, bullet.rect)

        # Рисование врагов
        for enemy in self.enemies:
            enemy.draw(self.screen)

        # Рисование счета и жизней
        self.score.draw(self.screen)
        self.health.draw(self.screen)

        pygame.display.flip()
