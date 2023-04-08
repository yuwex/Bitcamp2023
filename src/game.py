"""
A class for handling game mechanics
"""
import pygame
import time

BLACK = (0, 0, 0)
YELLOW = (255, 255, 102)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Email Pirates')

        self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.start()
    
    def start(self):
        self.before_start()

        self.running = True
        while self.running:
            self.game_loop()

        pygame.quit()

    def before_start(self):
        self.left = 590
        self.color = RED
        self.count = 0

    """
    Handles a game update with the number of read and unread
    emails since the last time the GameManager was polled
    """
    def update(self, read: int, unread: int):
        pass

    def draw_text(self, font_name: str, size: int, text: str, x: int, y: int, color: tuple):
        font = pygame.font.Font(font_name, size)
        surface = font.render(text, True, color)
        self.display.blit(surface, (x, y))

    def draw_rect(self, color: tuple, x: int, y: int, length: int = 10, width: int = 10):
        pygame.draw.rect(self.display, color, (x, y, length, width))

    # main loop for the game
    def game_loop(self):
        self.display.fill(BLACK)
        
        self.draw_text("src/Treasuremap.ttf", 30, "Score     0", 0, 0, YELLOW)
        
        self.draw_rect(YELLOW, 100, 200)
        self.draw_rect(RED, self.left, 100)
        self.left += 1
        # restarts the background

        print(self.left)

        if self.left > 600:
            self.left = 0

        pygame.display.update()  # updates the screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        time.sleep(0.01)

if __name__ == '__main__':
    game = Game()
    game.start()