import pygame


class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_velocity = 5
        self.y_velocity = 0
    def draw(self,display):
        pygame.draw.circle(display, (255, 255, 255), (self.x, self.y), self.radius)
        
    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        