import pygame
from settings import *
from sprites.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.bullets = MAX_BULLETS
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-1,0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(1, 0 )
        if keys[pygame.K_UP]:
            self.rect.move_ip(0,-1)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0,1)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        pass