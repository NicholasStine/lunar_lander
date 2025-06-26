import random
import pygame

from agent import Agent
from telemetry import Telemetry

class Spaceship():
    def __init__(self, screen, world):
        self.screen = screen
        self.dead = False
        self.velocity = (random.uniform(-0.01, 0.01), random.uniform(-0.01, 0.01))
        self.pos = (random.randint(50, self.screen.get_width() - 50), random.randint(40, 80))
        self.sprite = pygame.image.load('spaceship.png')
        self.sprite = pygame.transform.scale(self.sprite, (self.sprite.get_width() * 0.2, self.sprite.get_height() * 0.2))
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.surface = pygame.Surface((self.width, self.height))
        self.shape = pygame.Rect(*self.pos, self.width, self.height)
        self.surface.blit(self.sprite, (0,0))
        self.telemetry = Telemetry(self, world)
        self.agent = Agent(self)
    
    def die(self):
        self.dead = True
        self.agent.cache.pickle()
        return self

    def update(self):
        self.fall()
        self.pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1])
        self.moveRect()
        self.draw()
        self.telemetry.draw()

    def moveRect(self):
        updated_rect = pygame.Rect(*self.pos, self.width, self.height)
        self.shape = updated_rect

    def fall(self):
        self.velocity = (self.velocity[0], self.velocity[1] + 3e-5)

    def thrust(self):
        self.velocity = (self.velocity[0], self.velocity[1] - random.uniform(5e-5, 9e-5))

    def left(self):
        self.velocity = (self.velocity[0] - random.uniform(3e-5, 7e-5), self.velocity[1])

    def right(self):
        self.velocity = (self.velocity[0] + random.uniform(3e-5, 7e-5), self.velocity[1])

    def draw(self):
        self.screen.blit(self.sprite, self.pos)
