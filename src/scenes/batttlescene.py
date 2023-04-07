"""Battle Scene"""

import random

import pygame

from customs.camera import CameraGroup
from sprites.bullet import Bullet
from sprites.enemy import Enemy

from sprites.player import Player
from sprites.block import Block
from settings import WIDTH, HEIGHT, TITLESIZE, TITLE_MAPS
from utils.util import draw_text


class BattleScene:
    """Battle Scene"""
    def __init__(self):
        # Get surface
        self.screen = pygame.display.get_surface()

        # Groups sprite
        self.bullets_sprite = pygame.sprite.Group()
        self.enemies_sprite = pygame.sprite.Group()
        self.obtacles_sprite = pygame.sprite.Group()
        self.coin_sprite = pygame.sprite.Group()
        self.visible_sprite = CameraGroup()

        # Create Player
        self.player = Player(
            (WIDTH // 2, HEIGHT // 2), [self.visible_sprite], self.obtacles_sprite
        )

        # Generate Map
        self.create_map()

        # Spawn Enemy
        self.spawn_enemy(10)

    def create_map(self):
        """Create map"""
        for row_index, row_value in enumerate(TITLE_MAPS):
            for col_index, col_value in enumerate(row_value):
                pos_x = TITLESIZE * col_index
                pos_y = TITLESIZE * row_index

                if col_value == "x":
                    Block((pos_x, pos_y), [self.visible_sprite, self.obtacles_sprite])

    def spawn_enemy(self, count):
        """
        Spawn enemy
        args:
                count: int
        """
        # Spawn enemy x times
        for _ in range(count):
            Enemy(
                (random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)),
                [self.visible_sprite, self.enemies_sprite],
                [self.visible_sprite, self.coin_sprite],
            )

    def run(self):
        """Run scene"""
        self._draw()
        self._input()
        self._colission()
        draw_text(self.screen, f"HP: {self.player.get_hp()}", 20, (WIDTH - 100, 10))
        draw_text(
            self.screen, f"Coins: {self.player.get_coin()}", 20, (WIDTH - 100, 30)
        )

    def _draw(self):
        """Draw scene"""
        self.visible_sprite.custom_draw(self.player)
        self.visible_sprite.update(player=self.player)

    def _input(self):
        """Input scene"""

        # Validate if player is ready to recharge
        if self.player.ready_recharge:
            # Reset recharge
            self.player.reset_recharge()
            # Validate click left
            if pygame.mouse.get_pressed()[0]:
                # Get mouse position
                mouse_pos = pygame.mouse.get_pos()
                # Create bullet
                Bullet(
                    self.player.rect.center,
                    mouse_pos + self.visible_sprite.offset,
                    [self.visible_sprite, self.bullets_sprite],
                )

    def _colission(self):
        # Collision between bullets and enemies
        enemies = pygame.sprite.groupcollide(
            self.enemies_sprite, self.bullets_sprite, False, True
        )

        for enemy in enemies:
            enemy.get_damage(5)

        # Collision between bullets and obtacles
        pygame.sprite.groupcollide(
            self.bullets_sprite, self.obtacles_sprite, True, False
        )

        # Collision between player and enemies
        if pygame.sprite.spritecollide(self.player, self.enemies_sprite, False):
            self.player.get_damage(5)

        # Collision between player and coin
        coins = pygame.sprite.spritecollide(self.player, self.coin_sprite, True)

        # Get coin
        for coin in coins:
            self.player.set_coin(coin.value)
