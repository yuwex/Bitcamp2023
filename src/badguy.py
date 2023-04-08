import os
import pygame
class Badguy:

    def __init__(self, image_name):
        self.imageBadGuy = pygame.image.load(os.path.join(image_name))
        new_size = (self.imageBadGuy.get_width() * 9, self.imageBadGuy.get_height() * 9)
        self.imageBadGuy = pygame.transform.scale(self.imageBadGuy, new_size)
        self.x = 600
        self.y = 250


    def draw(self, surface: pygame.Surface):
        surface.blit(self.imageBadGuy, (self.x, self.y))


