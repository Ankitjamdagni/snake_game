import pygame
from pygame.locals import *
import time
import random

size=40

class Game:
    def __init__(self):
        pygame.init()
        self.surface=pygame.display.set_mode((1000,800))
        self.snake=snake(self.surface,1)
        self.snake.draw()
        self.apple=apple(self.surface)
        self.apple.draw()

    def display_score(self):
        font=pygame.font.SysFont("arial",30)
        score=font.render(f"score: {self.snake.length-2}", True,(255,255,255))
        self.surface.blit(score,(850,10))

    def run(self):
        
        running=True
        while running:
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        running=False

                    if event.key==K_UP:
                        self.snake.move_up()

                    if event.key==K_DOWN:
                        self.snake.move_down()

                    if event.key==K_RIGHT:
                        self.snake.move_right()

                    if event.key==K_LEFT:
                        self.snake.move_left()
                        
                elif event.type==QUIT:
                    running=False
            self.play()
            time.sleep(0.2)
    def play(self):
        self.snake.walk()
        self.apple.draw()

        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.snake.increase_length()
            self.apple.move()

    def is_collision(self,x1,y1,x2,y2):
        if x1>=x2 and x1<=x2*size:
            if y1>=y2 and y1<=y2*size:
                return True
        return False


class snake:
    def __init__(self,parent_screen,length):
        self.parent_screen=parent_screen
        self.block=pygame.image.load("resources/block.jpg").convert()
        self.length=length
        self.x=[size]*length
        self.y=[size]*length
        self.direction="down"
    
    
        
    def increase_length(self):
        self.length +=1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_screen.fill((52,235,195))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()
    def move_up(self):
        self.direction="up"
    def move_down(self):
        self.direction="down"
    def move_right(self):
        self.direction="right"
    def move_left(self):
        self.direction="left"
    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        if self.direction=="left":
            self.x[0]-=size
        elif self.direction=="right":
            self.x[0]+=size
        elif self.direction=="up":
            self.y[0]-=size
        elif self.direction=="down":
            self.y[0]+=size
        
        self.draw()

class apple:
    def __init__(self,parent_screen):
        self.parent_screen=parent_screen
        self.image=pygame.image.load("resources/apple.jpg").convert()
        self.x=size*3
        self.y=size*3

    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x=random.randint(1,24)*size
        self.y=random.randint(1,19)*size




if __name__=="__main__":
    game=Game()
    game.run()
 
   