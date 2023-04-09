import pygame
import os

class Image:
    def __init__(self, path: str, x: int, y: int, width_multiplier: int = 1, height_multiplier: int = 1):
        self.image = pygame.image.load(path)
        size = (self.image.get_width() * width_multiplier, self.image.get_height() * height_multiplier)
        self.image = pygame.transform.scale(self.image, size)
        self.x = x
        self.y = y
    
    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, (self.x, self.y))
    
    def draw_at(self, surface: pygame.Surface, x_offset: int, y_offset: int):
        surface.blit(self.image, (self.x + x_offset, self.y + y_offset))