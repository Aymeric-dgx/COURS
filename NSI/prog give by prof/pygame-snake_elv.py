#Tileset source : https://itch.io/c/2043497/tileset
import pygame
import random
import time
import pdb

class Anneau :
    def __init__(self, pos = (0,0), dir = (0,1)):
        self.suivant = None
        self.dir = dir
        self.pos = pos
    def set_suivant(self, a) :
        self.suivant = a
    def get_suivant(self) :
        return self.suivant
    def set_dir(self, dir) :
        self.dir = dir
    def get_dir(self) :
        return self.dir
    def set_pos(self, pos) :
        self.pos = pos
    def get_pos(self) :
        return self.pos

def printGrid(grid : list):
    for l in range(len(grid)):
        print('|', end='')
        for c in range(len(grid)):
            print(grid[l][c], end = '|')
        print('')

def drawSnake(screen, a_snake : Anneau):
    '''Dessine le serpent sur le canva PyGame
        in : screen -> un canva pygame
        in : a_snake -> un serpent composé par des instances de classe Anneau
        out : None
    '''
    if a_snake != None :
        size = 10                                               #taille des carrés
        square = pygame.rect.Rect(  a_snake.get_pos()[0]*size,  #pos x
                                    a_snake.get_pos()[1]*size,  #pos y
                                    size,                       #largeur
                                    size)                       #hauteur

        pygame.draw.rect(game_screen, (252,15,192), square)     #arguments de draw.rect :   1/ canva Pygame
                                                                #                           2/ couleur du rectangle
                                                                #                           3/ le rectangle
        drawSnake(screen, a_snake.get_suivant())

def moveSnake(a_snake : Anneau, a_modifier : dict):
    '''Deplace le serpent en fonction de la direction des anneaux qui le composent
        in : a_snake -> un serpent composé par des instances de classe Anneau
        in : a_modifier -> un dictionnaire Python qui contient en clé la case de changement de direction (tuple), en valeur associée la nouvelle direction
        out : None
    '''
    if a_modifier.get(a_snake.get_pos(), None) != None :
        a_snake.set_dir(a_modifier[a_snake.get_pos()])
        if a_snake.get_suivant() == None :
            a_modifier.pop(a_snake.get_pos())
    a_snake.set_pos(tuple(map(lambda x, y : x+y, a_snake.get_pos(), a_snake.get_dir())))    #tuple(map(lambda x, y : x+y, a_snake.get_pos(), a_snake.get_dir()))
                                                                                            #a_snake.get_pos() et a_snake.get_dir() renvoient tous les deux un tuple
                                                                                            #lambda x, y : x+y est une fonction anonyme appelée lambda fonction, elle prend deux argument x et y et renvoit le résultat de l'opération x + y
                                                                                            #map(foo, arg1[, arg2[, arg3 ...]) est une fonction Python qui applique la fonction foo pour chacun des éléments des itérable en argument
                                                                                            #dans notre cas il en result l'opération arg1[0]+arg2[0], arg1[1]+arg2[1]
                                                                                            #tuple(valeurs) crée un tuple avec les résultats du mapping soit (arg1[0]+arg2[0], arg1[1]+arg2[1])

    if a_snake.get_suivant() != None :
        moveSnake(a_snake.get_suivant(), a_modifier)

def pos_fruit():
    pos_fruit= (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
    return pos_fruit

def draw_fruit(screen, pos_fruit):
    size = 10
    fruit = pygame.rect.Rect(pos_fruit[0]*size, pos_fruit[1]*size, size, size)
    pygame.draw.rect(screen, (252,15,192), fruit)
    








if __name__ == "__main__" :
    # Game Screen
    SCREEN_WIDTH = 300
    SCREEN_HEIGHT = 300
    CLOCK = pygame.time.Clock()
    REFRESH_RATE = 10

    pygame.init()
    game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print('Game screen :',game_screen)

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

    snake = Anneau()
    modifiers = {}

    loop = True
    while loop :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                loop = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                modifiers[snake.get_pos()] = (0, -1)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                modifiers[snake.get_pos()] = (0, 1)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                modifiers[snake.get_pos()] = (-1, 0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                modifiers[snake.get_pos()] = (1, 0)
            
        a = pos_fruit()
        draw_fruit(game_screen, a)
		############
		#-- DRAW --#
		############
        game_screen.fill((0,0,0))

        drawSnake(game_screen, snake)

        ##############
		#-- UPDATE --#
		##############
        moveSnake(snake, modifiers)

        # Update all game graphics
        pygame.display.update()
        
        CLOCK.tick(REFRESH_RATE)
    pygame.quit()