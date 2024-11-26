import pygame
from paddle import Paddle

pygame.init()
BLACK = (0, 0, 0)
WEIGHT = (255, 255, 255)
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
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and self.left_paddle.y - self.left_paddle.velocity >= 0:
                    self.left_paddle.move("UP")
            if keys[pygame.K_s] and self.left_paddle.y + self.left_paddle.velocity <= HEIGHT - PADDLE_HEIGHT:
                    self.left_paddle.move("DOWN")
            if keys[pygame.K_UP] and self.right_paddle.y - self.right_paddle.velocity >= 0:
                    self.right_paddle.move("UP")
            if keys[pygame.K_DOWN] and self.right_paddle.y + self.right_paddle.velocity <= HEIGHT - PADDLE_HEIGHT:
                    self.right_paddle.move("DOWN")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    break
    def draw(self, display,paddles):
        display.fill(BLACK)
        for paddle in paddles:
            paddle.draw(display)
            
        for i in range(10,HEIGHT,HEIGHT//20):
            if i % 2 == 0:
                pygame.draw.rect(display, WEIGHT, (WIDTH//2 - 2, i, 4, HEIGHT//20))
        pygame.display.update()


if __name__ == "__main__":
    game = Game(700, 500)
    game.play()
