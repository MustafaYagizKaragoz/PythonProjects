import pygame
from paddle import Paddle
from ball import Ball
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
        self.reset()
    def play(self):
        while self.run:
            self.clock.tick(self.FPS)
            self.draw(self.display, [self.left_paddle, self.right_paddle],self.ball)
            keys = pygame.key.get_pressed()
            self.ball.move()
            self.check_score()
            self.check_collision(self.ball, self.right_paddle, self.left_paddle)
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
    def draw(self, display,paddles,ball):
        display.fill(BLACK)
        #draw the paddles
        for paddle in paddles:
            paddle.draw(display)
        #draw the middle line
        for i in range(10,HEIGHT,HEIGHT//20):
            if i % 2 == 0:
                pygame.draw.rect(display, WEIGHT, (WIDTH//2 - 2, i, 4, HEIGHT//20))
        #draw the ball
        ball.draw(display)
        #draw the score
        font = pygame.font.Font(None, 74)
        left_score = font.render(str(self.left_score), True, WEIGHT)
        right_score = font.render(str(self.right_score), True, WEIGHT)
        self.check_winner()
        display.blit(left_score, (WIDTH//4, 10))
        display.blit(right_score, (3*WIDTH//4 - 50, 10))
        
        #update the display
        pygame.display.update()
    def check_score(self):
        if self.ball.x - self.ball.radius <= 0:
            self.right_score += 1
            self.ball.x = WIDTH//2
            self.ball.y = HEIGHT//2
            self.ball.x_velocity = 5
            self.ball.y_velocity = 0
        elif self.ball.x + self.ball.radius >= WIDTH:
            self.left_score += 1
            self.ball.x = WIDTH//2
            self.ball.y = HEIGHT//2
            self.ball.x_velocity = -5
            self.ball.y_velocity = 0
    def reset(self):
        self.left_score = 0
        self.right_score = 0
        self.left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.right_paddle = Paddle(WIDTH - PADDLE_WIDTH - 10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.ball = Ball(WIDTH//2, HEIGHT//2, 10)
    def check_winner(self):
        if self.left_score == 3:
            font = pygame.font.Font(None, 74)
            text = font.render("Left Player Wins", True, WEIGHT)
            self.display.blit(text, (WIDTH//2 - 200, HEIGHT//2))
            pygame.display.update()  
            pygame.time.delay(3000)  
            self.reset()
        elif self.right_score == 3:
            font = pygame.font.Font(None, 74)
            text = font.render("Right Player Wins", True, WEIGHT)
            self.display.blit(text, (WIDTH//2 - 200, HEIGHT//2))
            pygame.display.update()  
            pygame.time.delay(3000)  
            self.reset()
    def check_collision(self,ball,right_paddle,left_paddle):
        if ball.y - ball.radius >= HEIGHT:
            ball.y_velocity *= -1
        elif  ball.y - ball.radius <= 0:
            ball.y_velocity *= -1

        if ball.x_velocity < 0:
            if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
                if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                    ball.x_velocity *= -1
                    
                    mid_y = left_paddle.y + left_paddle.height/2
                    diff_y = mid_y - ball.y
                    reduced_speed = (left_paddle.height/2) / 5
                    y_velocity = diff_y / reduced_speed
                    ball.y_velocity = -1*y_velocity
        else:
            if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
                if ball.x + ball.radius >= right_paddle.x:
                    ball.x_velocity *= -1
                    
                    mid_y = right_paddle.y + right_paddle.height/2
                    diff_y = mid_y - ball.y
                    reduced_speed = (right_paddle.height/2) / 5
                    y_velocity = diff_y / reduced_speed
                    ball.y_velocity = -1*y_velocity
if __name__ == "__main__":
    game = Game(700, 500)
    game.play()
