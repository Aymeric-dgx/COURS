#Tileset source : https://itch.io/c/2043497/tileset
import pygame

# Game Screen
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
CLOCK = pygame.time.Clock()
REFRESH_RATE = 10

pygame.init()
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

a_square = pygame.rect.Rect(0,0,100,100)
#-- Rectangle attributs --#
# x,y
# top, left, bottom, right
# topleft, bottomleft, topright, bottomright
# midtop, midleft, midbottom, midright
# center, centerx, centery
# size, width, height
# w,h
#-------------------------#

loop = True
while loop :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            loop = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            pass
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            pass
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            pass
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            pass

    ############
    #-- DRAW --#
    ############
    game_screen.fill((0,0,50))

    pygame.draw.rect(game_screen, (252,15,192), a_square)

    ##############
    #-- UPDATE --#
    ##############
    x, y, w, h = a_square
    mx = 0
    my = 0
    if x + w < SCREEN_WIDTH - 1 :
        mx = 1
    else :
        mx = -(SCREEN_WIDTH - w - 1)

        if y + h < SCREEN_HEIGHT - 1 :
            my = h
        else :
            my = -(SCREEN_HEIGHT - h - 1)

    print('avant : ', a_square)
    #a_square.move(mx, my)
    a_square.x += mx
    a_square.y += my
    print('apres : ', a_square)

    # Update all game graphics
    pygame.display.update()
    CLOCK.tick(REFRESH_RATE)
pygame.quit()