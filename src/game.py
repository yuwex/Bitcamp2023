"""
A class for handling game mechanics
"""
import pygame
import time
import os
from badguy import Badguy

#colors for the animation
BLACK = (0, 0, 0)
YELLOW = (255, 255, 102)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
WHITE = (255,255,255)

#dimensions for screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

class Game:

    def __init__(self, unread_messages: int):
        pygame.init()
        pygame.display.set_caption('Email Pirates')

        self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Initialize unread messages
        self.unread_messages = unread_messages
        self.read_messages = 0
    
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
        self.score = 0

        #character
        self.imageChar = pygame.image.load(os.path.join('src/assets/pirate8.png'))
        new_size = (self.imageChar.get_width() * 9, self.imageChar.get_height() * 9)
        self.imageChar = pygame.transform.scale(self.imageChar, new_size)
        self.charPos = 120

        #bad guy 1
        self.badguy = Badguy('src/assets/protagonist_green.png')
        
        #landscape
        self.image = pygame.image.load(os.path.join('src/Assets/landscape.jpg'))

    """
    Handles a game update with the number of read and unread
    emails since the last time the GameManager was polled
    """
    def update(self, read: int, unread: int):
        self.read_messages = read
        self.unread_messages = unread

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
        #start of the display
        self.display.blit(self.image, (0, 0))
        self.draw_text("src/assets/WayfarersToyBoxRegular.ttf", 40, f"Score  {self.score}", 10, 10, BLACK)
        self.draw_text("src/assets/WayfarersToyBoxRegular.ttf", 20, f"Enemies  {self.unread_messages}", 10, 70, BLACK)
        self.display.blit(self.imageChar, (30, 250))

        #if an email comes in, spawn a new bad guy
        self.badguy.draw(self.display)

        if self.badguy.x != self.charPos + 40:
            self.badguy.x -= 1

        #if email is read then the bad guy goes away and score increases

        pygame.display.update()  # updates the screen

        # Update Screen
        pygame.display.update() 

        # Quit if red dot pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        # Wait 0.01 Seconds
        time.sleep(0.01)

if __name__ == '__main__':
    game = Game(5)
    game.start()