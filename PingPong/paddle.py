import pygame

class Paddle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.COLOR = (255, 255, 255)

    def draw(self, display):
        pygame.draw.rect(display, self.COLOR,
                              (self.x, self.y, self.width, self.height))
