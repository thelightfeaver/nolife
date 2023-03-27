import pygame
from customs.camera import CameraGroup

from sprites.player import Player
from sprites.block import Block
from settings import *



class BattleScene:
    def __init__(self):
        # Get surface
        self.screen = pygame.display.get_surface()

        # groups sprite
        self.obtacles_sprite = pygame.sprite.Group()
        self.visible_sprite = CameraGroup()

        # Generate Map
        self.create_map()

    def create_map(self):

        for row_index, row_value in enumerate(TITLE_MAPS):
            
            for col_index, col_value in enumerate(row_value):
                
                x = TITLESIZE * col_index
                y = TITLESIZE * row_index
                
                if col_value == "x":
                    Block((x, y), [self.visible_sprite, self.obtacles_sprite])
                elif col_value == "P":
                    self.player = Player((x,y), [self.visible_sprite], self.obtacles_sprite)
        
    def run(self):
        self._draw()

    def _draw(self):
        self.visible_sprite.custom_draw(self.player)
        self.visible_sprite.update()
