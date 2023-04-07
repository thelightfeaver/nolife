"""Block class for the game."""
import pygame
from settings import TITLESIZE


class Block(pygame.sprite.Sprite):
    """Block class for the game."""
    def __init__(self, pos: set(), groups) -> None:
        super().__init__(groups)
        self.image = pygame.surface.Surface((TITLESIZE, TITLESIZE))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
