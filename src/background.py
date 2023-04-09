from image import Image
import pygame

GROUND = "src/assets/landscape/grass.png"
SKY = "src/assets/landscape/sky.png"

class Background:

    def __init__(self, speed = 1):

        self.ground = [
            Image(GROUND, 600, 0),
            Image(GROUND, 0, 0)
        ]

        self.images = [
            Image(SKY, 0, 0),
        ]

        self.images.extend(self.ground)
        self.speed = speed

    def draw(self, surface: pygame.Surface, moving: bool = True):
        for image in self.images:
            image.draw(surface)
        
        if moving:
            for img in self.ground:
                img.x -= self.speed
                if img.x <= -600:
                    img.x = 600
