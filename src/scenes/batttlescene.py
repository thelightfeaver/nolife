import pygame

from sprites.player import Player


class BattleScene:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.player_sprite = pygame.sprite.GroupSingle(Player())

    def run(self):
        self._draw()
        # self._collision()

    def _draw(self):
        self.player_sprite.draw(self.screen)
        self.player_sprite.update()

   
