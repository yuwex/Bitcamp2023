"""
A class for handling game mechanics
"""
import pygame
import time

# Final variables

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
        # Call before_start before starting
        self.before_start()

        # Set running to true and run until false
        self.running = True
        while self.running:
            self.game_loop()

        # Quit
        pygame.quit()

    def before_start(self):
        # Define all variables here
        self.left = 590
        self.color = RED
        self.count = 0
        self.score = 1000

    """
    Handles a game update with the number of read and unread
    emails since the last time the GameManager was polled
    """
    def update(self, read: int, unread: int):
        pass

    def draw_text(self, font_name: str, size: int, text: str, x: int, y: int, color: tuple):
        # Create a new Font object
        font = pygame.font.Font(font_name, size)

        # Create a new Surface Object
        surface = font.render(text, True, color)

        # Display Surface object on the screen
        self.display.blit(surface, (x, y))

    def draw_rect(self, color: tuple, x: int, y: int, length: int = 10, width: int = 10):
        # Draw rectangle object on the screen
        pygame.draw.rect(self.display, color, (x, y, length, width))

    # main loop for the game
    def game_loop(self):
        self.display.fill(BLACK)
        
        # Draw text with score data
        self.draw_text("src/Treasuremap.ttf", 30, f"Score {self.score}", 0, 0, YELLOW)
        
        # Draw moving red rectangle
        self.draw_rect(RED, self.left, 100)
        self.left += 1

        # Loop red rectangle at end
        if self.left > 600:
            self.left = 0

        # Update Screen
        pygame.display.update() 

        # Quit if red dot pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        # Wait 0.01 Seconds
        time.sleep(0.01)

if __name__ == '__main__':
    game = Game()
    game.start()