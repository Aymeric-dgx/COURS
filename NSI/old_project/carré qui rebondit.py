import pygame

pygame.init()

SREEN_WIDTH = 640
SREEN_HEIGHT = 480
screen = pygame.display.set_mode((SREEN_WIDTH, SREEN_HEIGHT))
pygame.display.set_caption("Carré qui rebondit")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    

    pygame.display.update()
