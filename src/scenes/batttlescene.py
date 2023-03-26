import pygame
from settings import *

from sprites.player import Player


class BattleScene():
    def __init___(self):
        self.screen = pygame.display.get_surface()
        self.player_sprite = pygame.sprite.GroupSingle()
        self.player_sprite.add(Player())
        


    def run(self):
        self.draw()
        self.collision()

    def draw(self):
        self.player_sprite.draw(self.screen)
        self.player_sprite.update()

    def collision(self):
        pass
