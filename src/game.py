"""
A class for handling game mechanics
"""
import os
import random
import time

import pygame

from badguy import Badguy
from image import Image
from background import Background

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
        self.enemies: list[Badguy] = []
        self.count = 1
        self.distance = 160

        self.knife = Image('src/assets/sword_blue.png', 120, 270, 5, 5)
        self.hat = Image('src/assets/HAT.png', 30, 195, 7, 7)

        #character
        self.imageChar = pygame.image.load(os.path.join('src/assets/pirate8.png'))
        new_size = (self.imageChar.get_width() * 9, self.imageChar.get_height() * 9)
        self.imageChar = pygame.transform.scale(self.imageChar, new_size)
        
        self.charPos = 120

        #bad guys
        self.new_enemies(self.unread_messages)

        #landscape
        self.background = Background(0.75)

        # clouds
        self.upper_clouds: list[Image] = []
        self.lower_clouds: list[Image] = []

        self.initialize_upper_clouds()
        self.initialize_lower_clouds()


    """
    Handles a game update with the number of read and unread
    emails since the last time the GameManager was polled
    """
    def update(self, read: int, unread: int):
        old_unread = self.unread_messages

        self.read_messages = read
        self.unread_messages = unread
        
        self.kill_enemies(read)
        
        count = self.unread_messages - old_unread - read
        if count > 0:
            self.new_enemies(count)

    def kill_enemies(self, count: int):
        self.score += count
        for _ in range(count):
            self.knife.draw(self.display)
            self.enemies.pop(0)
    
    def new_enemies(self, count: int):
        # When email comes in, spawn a new bad guy

        # Possible Bad Guy Costumes
        costumes = [
            'src/assets/protagonist_green.png',
            'src/assets/protagonist_blue.png',
            'src/assets/protagonist_red.png',
            'src/assets/protagonist_yellow.png',
            'src/assets/skeleton.png',
            'src/assets/pirate3.png',
            'src/assets/pirate4.png',
            'src/assets/pirate4.png'
        ]

        for _ in range(count):
            offset = len(self.enemies) * 160

            costume = random.choice(costumes)
            guy = Badguy(costume)

            if "skeleton" in costume:
                guy.y += 20
            guy.x += offset

            self.enemies.append(guy)

    def draw_enemies(self, speed: int = 0.75):
        for enemy in self.enemies:
            if (enemy.x > (self.enemies.index(enemy) + 1) * 160):
                enemy.x -= speed

            enemy.draw(self.display)


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

    def initialize_lower_clouds(self):
        for i in range (random.randint(2,4)):
            cloud_num = random.randint(1,8)
            x_value = random.randint(-100,1200)
            y_value = random.randint(100,205)
            size_multiplier = random.randint(5,9)
            self.lower_clouds.append(Image(f"src/assets/landscape/clouds/clouds{cloud_num}.png", x_value, y_value, size_multiplier, size_multiplier))
        
    def initialize_upper_clouds(self):
        for i in range (random.randint(2,4)):
            cloud_num = random.randint(1,8)
            x_value = random.randint(-100,1200)
            y_value = random.randint(0,100)
            size_multiplier = random.randint(5,9)
            self.upper_clouds.append(Image(f"src/assets/landscape/clouds/clouds{cloud_num}.png", x_value, y_value, size_multiplier, size_multiplier))

    def move_upper_clouds(self):
        for cloud in self.upper_clouds:
            cloud.x -= 0.2
            if cloud.x <= -450:
                cloud.x = 1200

    def move_lower_clouds(self):
        for cloud in self.lower_clouds:
            cloud.x -= 0.4
            if cloud.x <= -450:
                cloud.x = 1200

    # main loop for the game
    def game_loop(self):
        #start of the display
        self.background.draw(self.display)
        for cloud in self.lower_clouds:
            cloud.draw(self.display)
        for cloud in self.upper_clouds:
            cloud.draw(self.display)

        self.draw_text("src/assets/WayfarersToyBoxRegular.ttf", 40, f"Score  {self.score}", 10, 10, BLACK)
        self.draw_text("src/assets/WayfarersToyBoxRegular.ttf", 20, f"Enemies  {self.unread_messages}", 10, 70, BLACK)
        self.display.blit(self.imageChar, (30, 250))

        # Draw enemies
        self.draw_enemies()
        self.hat.draw(self.display)
        
        # move clouds   
        self.move_upper_clouds()
        self.move_lower_clouds()

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