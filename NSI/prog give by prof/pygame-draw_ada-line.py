#Tileset source : https://itch.io/c/2043497/tileset
import pygame

def colorSquare(x, y, a, b, c) :
    result = a*x+b*y+c
    return_val = 0
    if result < 0:
        return_val = -1
    elif result > 0 :
        return_val = 1
    return return_val

def drawSquare(screen, x, y, side, color):
    a_square = pygame.rect.Rect(x*side,y*side,side,side)
    pygame.draw.rect(screen, color, a_square)
#################
# <Game Screen> #
#################
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
CLOCK = pygame.time.Clock()
REFRESH_RATE = 10

pygame.init()
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
##################
# </Game Screen> #
##################
#y = (ax + c)/(-b)
a = 1
b = -1
c = 0
square_side = 10
colors = {-1 : (255,246,0), 0:(57,255,20), 1:(255,0,79)}


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
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            a += 0.125
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            a -= 0.125
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            b += 0.125
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            b -= 0.125
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            c += 0.125
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            c -= 0.125

		############
		#-- DRAW --#
		############
        game_screen.fill((0,0,0))

        for x in range(SCREEN_WIDTH // square_side):
            for y in range(SCREEN_HEIGHT // square_side):
                set_color = colorSquare(x, y, a, b, c)
                drawSquare(game_screen, x, (SCREEN_HEIGHT // square_side - 1)-y, square_side, colors[set_color])

        font = pygame.font.Font(None, 36)
        text = font.render("a: "+str(a)+", b: "+str(b)+", c: "+str(c), 1, (10, 10, 10))
        textpos = text.get_rect(centerx=game_screen.get_width() / 2, centery=10)#game_screen.get_height() / 2)
        game_screen.blit(text, textpos)

    # Update all game graphics
    pygame.display.update()
    CLOCK.tick(REFRESH_RATE)
pygame.quit()