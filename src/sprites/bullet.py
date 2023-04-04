import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, origin, target, groups):
        super().__init__(groups)
        self.image = pygame.surface.Surface((10, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center = origin)
        self.speed = 15
        self.direction = pygame.math.Vector2(target) - pygame.math.Vector2(origin)
        self.direction = self.direction.normalize()

    def update(self, *args, **kwargs):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed