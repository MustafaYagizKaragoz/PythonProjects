import pygame
import random
from enum import Enum
from collections import namedtuple
pygame.init()

font=pygame.font.Font("arial.ttf",25)

class Direction(Enum):
    RIGHT=1
    LEFT=2
    UP=3
    DOWN=4

Point=namedtuple("Point","x,y")

WHITE=(255,255,255)
RED=(200,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
BLACK=(0,0,0)

BLOCK_SIZE=20
SPEED=20

class SnakeGame:
    def __init__(self,w=1280,h=720) -> None:
        self.w=w
        self.h=h
        self.display=pygame.display.set_mode((self.w,self.h))
        self.clock=pygame.time.Clock()
        
        self.direction=Direction.RIGHT
        self.head=Point(self.w/2,self.h/2)
        self.snake=[self.head,
                    Point(self.head.x-BLOCK_SIZE,self.head.y),
                    Point(self.head.x-(2*BLOCK_SIZE),self.head.y)]
        self.score=0
        self.food=None
        self.place_food()
        
        
    def place_food(self):
        x=random.randint(0,(self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y=random.randint(0,(self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        self.food=Point(x,y)

            
    
    def play_step(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
        self.move(self.direction)
        self.snake.insert(0,self.head)
        
        is_over=False
        
        if self.is_collision():
            is_over=True
            return is_over,self.score
        
        if self.head == self.food:
            self.score+=1
            self.place_food()
        else:
            self.snake.pop()
            
        self.update_ui()
        self.clock.tick(SPEED)
        return is_over,self.score


    def is_collision(self):
        if self.head.x > self.w -BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h-BLOCK_SIZE or self.head.y < 0:
            return True
        
        if self.head in self.snake[1:]:
            return True
        
        return False
    
    def update_ui(self):
        self.display.fill(BLACK)
        
        for pt in self.snake:
            pygame.draw.rect(self.display,BLUE,pygame.Rect(pt.x,pt.y,BLOCK_SIZE,BLOCK_SIZE))
            pygame.draw.rect(self.display,GREEN,pygame.Rect(pt.x+4,pt.y+4,12,12))
        pygame.draw.rect(self.display,RED,pygame.Rect(self.food.x,self.food.y,BLOCK_SIZE,BLOCK_SIZE))
        
        text = font.render("Score: "+str(self.score),True,WHITE)
        self.display.blit(text,[0,0])
        pygame.display.flip()
        
    def move(self,direction):
        x=self.head.x
        y=self.head.y
        if direction == Direction.RIGHT:
            x+=BLOCK_SIZE
        elif direction == Direction.LEFT:
            x-=BLOCK_SIZE
        elif direction == Direction.UP:
            y-=BLOCK_SIZE
        elif direction == Direction.DOWN:
            y+=BLOCK_SIZE
        self.head = Point(x,y)
        
if __name__ == '__main__':
    sg=SnakeGame()
    
    while True:
        is_over,score=sg.play_step()
        
        if is_over == True:
            break
        
    print("Final Score:  ",score)
    pygame.quit()    
    
