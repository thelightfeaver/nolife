import pygame 
from settings import FONT_NAME, WHITE

def draw_text(surface, text, size, pos):
    font = pygame.font.Font(FONT_NAME, size)
    text_surface = font.render(text, True, "green", "black" )
    text_rect = text_surface.get_rect()
    text_rect.midtop = pos
    surface.blit(text_surface, text_rect)