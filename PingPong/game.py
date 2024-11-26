import pygame
from paddle import Paddle

pygame.init()
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 700, 500
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
class Game:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Ping Pong")
        self.clock = pygame.time.Clock()
        self.run = True
        self.FPS = 60
        self.left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.right_paddle = Paddle(WIDTH - PADDLE_WIDTH - 10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        
        
    def play(self):
        while self.run:
            self.clock.tick(self.FPS)
            self.draw(self.display, [self.left_paddle, self.right_paddle])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    break
        pygame.quit()

    def draw(self, display,paddles):
        display.fill(BLACK)
        for paddle in paddles:
            paddle.draw(display)
        pygame.display.update()


if __name__ == "__main__":
    game = Game(700, 500)
    game.play()
