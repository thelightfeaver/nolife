import pygame
from settings import *

class Block(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y) -> None:
        super().__init__()
        self.image = pygame.surface.Surface((TITLESIZE, TITLESIZE))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
