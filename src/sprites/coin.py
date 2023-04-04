import pygame 


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, value, image, groups):
        super().__init__(groups)
        self.image = pygame.surface.Surface((5, 5))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.value = value