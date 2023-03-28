import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos:set(), groups) -> None:
        super().__init__(groups)
        self.image = pygame.surface.Surface((50,50))
        self.image.fill((255,50,0))
        self.rect = self.image.get_rect(center=pos)
        self.speed = random.randint(2, 6)
        
    def update(self, *args, **kwargs ):
        if kwargs["player"]:
            self.move(kwargs["player"].rect.x, kwargs["player"].rect.y)

    def move(self, target_x, target_y):
         
        if self.rect.x < target_x:
            self.rect.x += self.speed
        elif self.rect.x > target_x:
            self.rect.x -= self.speed

        if self.rect.y < target_y:
            self.rect.y += self.speed
        elif self.rect.y > target_y:
            self.rect.y -= self.speed
