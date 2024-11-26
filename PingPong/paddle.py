import pygame

class Paddle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.COLOR = (255, 255, 255)
        self.velocity = 4

    def draw(self, display):
        pygame.draw.rect(display, self.COLOR,
                              (self.x, self.y, self.width, self.height))
    def move(self, direction):
        if direction == "UP":
            self.y -= self.velocity
        elif direction == "DOWN":
            self.y += self.velocity