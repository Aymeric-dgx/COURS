import pygame

game_screen = None

def drawSnake(screen, a_snake):
    if a_snake != None :
        size = 10
        square = pygame.rect.Rect(  a_snake.get_pos()[0]*size,
                                    a_snake.get_pos()[1]*size,
                                    size,
                                    size)
        pygame.draw.rect(game_screen, (252,15,192), square)
        drawSnake(screen, a_snake.get_suivant())

def moveSnake(a_snake, a_modifier):
    if a_modifier.get(a_snake.get_pos(), None) != None :
        a_snake.set_dir(a_modifier[a_snake.get_pos()])
        if a_snake.get_suivant() == None :
            a_modifier.pop(a_snake.get_pos())

    a_snake.set_pos(tuple(map(lambda x, y : x+y, a_snake.get_pos(), a_snake.get_dir())))

    if a_snake.get_suivant() != None :
        moveSnake(a_snake.suivant(), a_modifier)