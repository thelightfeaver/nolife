import random

import pygame

from sprites.coin import Coin


class Enemy(pygame.sprite.Sprite):
    """Enemy class"""

    def __init__(self, pos: set(), groups, sprite_group_items) -> None:
        super().__init__(groups)
        self.image = pygame.surface.Surface((50, 50))
        self.image.fill((255, 50, 0))
        self.rect = self.image.get_rect(center=pos)
        self.speed = random.randint(1, 2)
        self._hp = 25
        self.sprite_group_items = sprite_group_items

    def update(self, *args, **kwargs):
        """update the enemy"""
        if kwargs["player"]:
            self.move(kwargs["player"].rect.x, kwargs["player"].rect.y)

    def move(self, target_x, target_y):
        """
        Move the enemy
        args:
            target_x: int
            target_y: int
        """
        if self.rect.x < target_x:
            self.rect.x += self.speed
        elif self.rect.x > target_x:
            self.rect.x -= self.speed

        if self.rect.y < target_y:
            self.rect.y += self.speed
        elif self.rect.y > target_y:
            self.rect.y -= self.speed

    def get_damage(self, at):
        """
        Get damage.
        args:
            at: int
        """
        self._hp -= at
        if self._hp <= 0:
            Coin(self.rect.center, 10, None, self.sprite_group_items)
            self.kill()
