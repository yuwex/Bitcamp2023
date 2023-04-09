from image import Image
import pygame
import random
import os

class Badguy(Image):

    def __init__(self, image, x_offset: int = 0, y_offset: int = 0):
        super().__init__(image, 600 + x_offset, 250 + y_offset, 9, 9)
        self.random_offset = random.randint(1, 100)
    


