import pygame
from settings import *
from sprites.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos,groups, obtacles: pygame.sprite.Sprite):
        super().__init__(groups)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.direction = pygame.math.Vector2()
        self.speed = 3
        self.obtacles = obtacles

    def _input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def _move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self._collision('H')
        self.rect.y += self.direction.y * speed
        self._collision('V')

    def update(self):
        self._input()
        self._move(self.speed)
        
    def _collision(self, orientation = "V" or "H"):
        if orientation == "V":
            for sprite in self.obtacles:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
        if orientation == "H":
            for sprite in self.obtacles:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right