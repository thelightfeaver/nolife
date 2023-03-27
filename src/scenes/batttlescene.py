import pygame

from sprites.player import Player
from sprites.block import Block
from settings import *


class BattleScene:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.player_sprite = pygame.sprite.GroupSingle(Player())
        self.maps_sprite = pygame.sprite.Group()

        for row_index, row_value in enumerate(TITLE_MAPS):
            for col_index, col in enumerate(row_value):
                x = TITLESIZE * col_index
                y = TITLESIZE * row_index
                if col == "x":
                    self.maps_sprite.add(Block(x, y))

        

    def run(self):
        self._draw()
        # self._collision()

    def _draw(self):

        self.player_sprite.draw(self.screen)
        self.player_sprite.update()
        self.maps_sprite.draw(self.screen)
        self.maps_sprite.update()

        
   
    def _colision(self):
        pass