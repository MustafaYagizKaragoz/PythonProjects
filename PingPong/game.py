import pygame

pygame.init()
BLACK = (0, 0, 0)


class Game:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Ping Pong")
        self.clock = pygame.time.Clock()
        self.run = True
        self.FPS = 60

    def play(self):
        while self.run:
            self.clock.tick(self.FPS)
            self.draw(self.display)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    break
        pygame.quit()

    def draw(self, display):
        display.fill(BLACK)
        pygame.display.update()


if __name__ == "__main__":
    game = Game(700, 500)
    game.play()
