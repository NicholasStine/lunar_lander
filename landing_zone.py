
import pygame


class LandingZone():
    def __init__(self, screen, width, position):
        self.screen = screen
        self.position = position
        self.width = width 
        self.shape = pygame.Rect(*self.position, self.width, 30)

    def update(self):
        self.draw()
    
    def draw(self, color=(100, 100, 100)):
        pygame.draw.rect(self.screen, color, self.shape)
    