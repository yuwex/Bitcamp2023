from image import Image
import pygame
import os

class Badguy(Image):

    def __init__(self, image):
        super().__init__(image, 600, 250, 9, 9)

