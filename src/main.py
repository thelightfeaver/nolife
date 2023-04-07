import pygame

from scenes.batttlescene import BattleScene
from settings import WIDTH, HEIGHT, FPS


class Game:
    """
    Main game class
    """

    def __init__(self) -> None:
        pygame.init()
        self.setup()

    def setup(self):
        """
        Setup the game
        """
        pygame.display.set_caption("No Life")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.battle = BattleScene()

    def run(self):
        """
        Run the game loop
        """
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
