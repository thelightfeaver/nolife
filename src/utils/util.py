"""Utility functions for the game."""
import pygame
from settings import FONT_NAME


def draw_text(surface, text, size, pos):
    """Draw text on the screen
    args:
        surface: pygame.Surface
        text: str
        size: int
        pos: tuple
    """
    font = pygame.font.Font(FONT_NAME, size)
    text_surface = font.render(text, True, "green", "black")
    text_rect = text_surface.get_rect()
    text_rect.midtop = pos
    surface.blit(text_surface, text_rect)
