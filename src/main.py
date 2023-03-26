import pygame
from settings import *
from scenes.batttlescene import BattleScene


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.setup()

    def setup(self):
        pygame.display.set_caption("Zombie Shooter")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.battle = BattleScene()

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                

            self.screen.fill("white")
            self.battle.run()
            pygame.display.update()

        
        pygame.quit()


if __name__ == "__main__":
    g = Game()
    g.run()