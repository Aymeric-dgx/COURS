import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
CLOCK = pygame.time.Clock()
REFRESH_RATE = 10
square_side = 10


pygame.init()
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))




def drawSquare(screen, x, y, side, color):
    a_square = pygame.rect.Rect(x*side,y*side,side,side)
    pygame.draw.rect(screen, color, a_square)



loop = True
while loop :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False


    game_screen.fill((50,0,150))
    pygame.update.display()