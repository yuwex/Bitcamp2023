"""
A class for handling game mechanics
"""
import pygame
import time
pygame.init()
#params for the game screen
width = 600
height = 400
display = pygame.display.set_mode((width, height))
#colors for the game beta
black = (0,0,0)
yellow = (255,255,102)
red = (213,50,80)
green = (0,255,0)
blue =(50,153,213)
#style for the game screen
scoreStyle = pygame.font.SysFont('Treasuremap.ttf', 35)
pygame.display.set_caption('Email Pirates')

#displaying the score
def yourScore(score):
        value = scoreStyle.render('Score: ' + str(score), True, yellow)
        display.blit(value, [0,0])

#makes the moving background
def background(left, color):
      pygame.draw.rect(display, color, [left, 100, 10, 10])

class Game:
    """
    Handles a game update with the number of read and unread
    emails since the last time the GameManager was polled
    """
    def update(self, read: int, unread: int):
        pass

    #main loop for the game
    def gameLoop():
        left = 590
        color = red
        count = 0

        gameNotClose = True
        display.fill(black)
        pygame.draw.rect(display, yellow, [90, 320, 10, 10])
        yourScore(5)
        pygame.display.update() #updates the screen

        while gameNotClose == True:
            background(left, color)
            time.sleep(.05)
            left -= 20
            #restarts the background
            if left <= 0:
                count += 1
                if count == 4:
                     count = 1
                left = 590
                if count == 1:
                    color = blue
                elif count == 2:
                    color = green
                else:
                    color = red

            pygame.display.update() #updates the screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameNotClose = False
        pygame.quit
        quit()
