import pygame
from settings import *

class Block(pygame.sprite.Sprite):
    def __init__(self, pos:set(), groups) -> None:
        super().__init__(groups)
        self.image = pygame.surface.Surface((TITLESIZE, TITLESIZE))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
