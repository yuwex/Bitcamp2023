import pygame

class SurfaceWrapper:

    def __init__(self, surface: pygame.Surface, x: int, y: int):
        self.surface = surface
        self.x = x
        self.y = y

    def draw_at(self, surface: pygame.Surface, x_offset: int = 0, y_offset: int = 0):        
        surface.blit(self.surface, (self.x + x_offset, self.y + y_offset))