from image import Image
import pygame

class Background:

    def __init__(self, speed = 1):

        self.ground = [
            Image("src/assets/landscape/grass.png", 600, 0),
            Image("src/assets/landscape/grass.png", 0, 0)
        ]

        self.images = [
            Image("src/assets/landscape/sky.png", 0, 0),
        ]

        self.images.extend(self.ground)
        self.speed = speed

    def draw(self, surface: pygame.Surface):
        for image in self.images:
            image.draw(surface)
        
        for img in self.ground:
            img.x -= self.speed
            if img.x <= -600:
                img.x = 600
