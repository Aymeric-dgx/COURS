

import pygame
import time

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

class Snake:
    def __init__(self, pose = (0,0), direction = (1,0)):
        self.suivant = None
        self.pose = pose
        self.direction = direction

    def set_suivant(self, a : tuple):
        self.suivant = a
    def get_suivant(self):
        return self.suivant
    def set_dir(self, dir : tuple):
        self.direction = dir
    def get_dir(self):
        return self.direction
    def set_pos(self, pos : tuple):
        self.pose = pos
    def get_pos(self):
        return self.pose
    
    def add_suivant(self):
        if self.suivant == None :
            self.suivant = Snake(self.get_pos()- self.get_dir(), self.get_dir())
        else :
            self.suivant.add_suivant()

    def move_snake(self):
        self.set_pos((self.pose[0] + self.direction[0], self.pose[1] + self.direction[1]))
        if self.suivant != None :
            self.suivant.move_snake()




def draw_square(screen, pos, size, color):
    square = pygame.rect.Rect(pos[0]*size, pos[1]*size, size, size)
    pygame.draw.rect(screen, color, square)




head = Snake((0,0), (1,0))
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            head.set_dir((0,-1))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            head.set_dir((0,1))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            head.set_dir((-1,0))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            head.set_dir((1,0))
        
        #pour tester
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            head.add_suivant()



    screen.fill((0,0,0))
    draw_square(screen, head.get_pos(), 10, (252,15,192))
    head.move_snake()
    
    
    pygame.display.flip()
    time.sleep(0.1)