import pygame 



class CameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

        self.screen = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(50, 50)
        self.half_screen = {
            "width" :self.screen.get_size()[0] // 2,
            "hight" : self.screen.get_size()[1] // 2
        }


    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_screen["width"]
        self.offset.y = player.rect.centery - self.half_screen["hight"]
        
        for sprite in self.sprites():

            offpos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offpos)
