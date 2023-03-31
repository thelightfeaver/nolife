import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Example")

running = True
while running:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.line(screen,"white" , [20, 20], [50,50], 10)
    screen.fill((0, 0, 0))
    pygame.display.flip()


pygame.quit()