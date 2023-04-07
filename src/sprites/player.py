"""Player class"""
import time

import pygame


class Player(pygame.sprite.Sprite):
    """Player class"""

    def __init__(self, pos, groups, obtacles):
        super().__init__(groups)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.direction = pygame.math.Vector2()
        self.speed = 9
        self.obtacles = obtacles
        self.time_recharge = time.time()
        self.time_invulnerable = time.time()
        self.ready_recharge = True
        self.ready_invulnerable = True
        self._hp = 100
        self._died = False
        self._value = 0

    def _input(self):
        """Get the player's input"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def _move(self, speed):
        """Move the player"""
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self._collision("H")
        self.rect.y += self.direction.y * speed
        self._collision("V")

    def update(self, *args, **kwargs):
        """Update the player's position"""
        if not self._died:
            self._input()
            self._move(self.speed)
            self._recharge_shoot()
            self._recharge_invulnerable()

    def _collision(self, orientation="V" or "H"):
        """Collision with the obtacles"""
        if orientation == "V":
            for sprite in self.obtacles:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

        if orientation == "H":
            for sprite in self.obtacles:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

    def get_damage(self, at):
        """Get damage from the player"""
        if self.ready_invulnerable:
            self._hp -= at
            self.ready_invulnerable = False
            self.time_invulnerable = time.time()

            if self._hp <= 0:
                self._died = True

    def _recharge_shoot(self):
        """Recharge the shoot time"""
        if time.time() - self.time_recharge > 0.1:
            self.time_recharge = time.time()
            self.ready_recharge = True

    def _recharge_invulnerable(self):
        """Recharge the invulnerability time"""
        if time.time() - self.time_invulnerable > 0.5:
            self.time_invulnerable = time.time()
            self.ready_invulnerable = True

    def get_hp(self):
        """Return the player's hp"""
        return self._hp

    def reset_recharge(self):
        """Reset the recharge time"""
        self.time_recharge = time.time()
        self.ready_recharge = False

    def set_coin(self, coin_value):
        """Set the player's coin value"""
        self._value += coin_value

    def get_coin(self):
        """Return the player's coin value"""
        return self._value
