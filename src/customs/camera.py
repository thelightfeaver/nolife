import pygame 


class CameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

        self.screen = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(50, 50)
        self.half_screen = pygame.math.Vector2(self.screen.get_width() // 2, self.screen.get_height() // 2)

    def custom_draw(self, player):

        self.offset = player.rect.center - self.half_screen
        
        for sprite in self.sprites():

            offpos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offpos)
