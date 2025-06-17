import math
import random
import pygame

from landing_zone import LandingZone

WORLD_COLOR = (150, 150, 150)
COLLIDE_COLOR = (45,45,45)
TARGET_COLOR = [(255, 100, 100), (255, 255, 100), (100, 255, 100)]

class World():
    def __init__(self, screen):
        self.screen = screen
        _w, _h = screen.get_size()
        self.screen_w = _w
        self.screen_h = _h
        self.shapes = []

        self.generateTerrain()
        self.generateLandingZones()

    def update(self):
        self.draw()

    def draw(self):
        for i, zone in enumerate(self.landing_zones):
            zone.draw(TARGET_COLOR[i])
        for rect in self.shapes:
            pygame.draw.rect(self.screen, COLLIDE_COLOR, rect)
        pygame.draw.polygon(self.screen, WORLD_COLOR, self.floor_points)

    def generateLandingZones(self):
        self.landing_zones = []
        width = 3
        for i in range(4,1,-1):
            self.landing_zones.append(LandingZone(self.screen, width * 2 * math.exp(i) * 0.8, ((self.screen_w / 2) - (width * math.exp(i) * 0.8), self.floor_rect.top - 10)))
        # x_step = self.screen_w / 3
        # x_pos = x_step / 2
        # for _ in range(3):
        #     offset = 0
        #     position = (x_pos + offset, self.floor_rect.top - 10)
        #     zones.append([width, position])
        #     width += width
        #     x_pos += x_step
        # self.landing_zones = [LandingZone(self.screen, width, position) for [width, position] in zones]
        # random.shuffle(self.landing_zones)
        # self.landing_zones = sorted(self.landing_zones, key=lambda _: random.random())

    def generateTerrain(self):
        other = []
        steps = 20
        zero_altitude = self.screen_h - 25
        for step_i in range(steps):
            step_x = step_i * (self.screen_w / steps)
            rand_y = random.randint(zero_altitude - 10, zero_altitude + 10)
            other.append((step_x, rand_y))

        self.floor_points = [
            (self.screen_w + 10, zero_altitude),
            (self.screen_w + 10, self.screen_h + 10),
            (-10, self.screen_h + 10), 
            (-10, zero_altitude),
            *other
        ]

        self.floor_rect = pygame.Rect(0, zero_altitude - 60, self.screen_w, 120)
        self.ceiling_rect = pygame.Rect(0, 0, self.screen_w, 10)
        self.left_rect = pygame.Rect(0, 0, 10, self.screen_h)
        self.right_rect = pygame.Rect(self.screen_w - 10, 0, 10, self.screen_h)
        self.shapes.append(pygame.draw.rect(self.screen, COLLIDE_COLOR, self.floor_rect))
        self.shapes.append(pygame.draw.rect(self.screen, COLLIDE_COLOR, self.ceiling_rect))
        self.shapes.append(pygame.draw.rect(self.screen, COLLIDE_COLOR, self.left_rect))
        self.shapes.append(pygame.draw.rect(self.screen, COLLIDE_COLOR, self.right_rect))
