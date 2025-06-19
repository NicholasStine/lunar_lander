import pygame
pygame.font.init()

class Telemetry():
    def __init__(self, ship, world):
        self.ship = ship
        self.world = world
        self.font = pygame.font.SysFont('Comic Sans MS', 15)

        self.score = 0
        self.altitude = 0
        self.distance = 0
        
    def draw(self):
        altitude = self.world.floor_rect.top - (self.ship.pos[1] + self.ship.sprite.get_height())
        altitude = (altitude / (10 * (self.world.screen_h - self.world.floor_rect.top)))
        velocity = abs(self.ship.velocity[1] / .2)
        distance = (self.world.screen_w / 2) - (self.ship.pos[0] + self.ship.sprite.get_width() / 2)
        distance = distance / (self.world.screen_w / 2)
        score = (4 - ((altitude * 2) + velocity + abs(distance))) / 4

        self.score = score
        self.altitude = altitude
        self.distance = distance

        color = (255 - (255 * score), 255 * score, 0)

        altitude = str(altitude)[:4]
        velocity = str(velocity)[:4 if velocity > 0 else 5]
        distance = str(distance)[:4 if distance > 0 else 5]
        score = str(score)[:4]
        
        altitude_text = self.font.render(f"alt: {altitude}", False, color) # (255, 255, 255)
        velocity_text = self.font.render(f"vel: {velocity}", False, color) # (255, 255, 255)
        distance_text = self.font.render(f"dist: {distance}", False, color) # (255, 255, 255)
        score_text = self.font.render(f"score: {score}", False, color) # (255, 255, 255)

        self.ship.screen.blit(altitude_text, (self.ship.pos[0] - 10, self.ship.pos[1] - 20))
        self.ship.screen.blit(velocity_text, (self.ship.pos[0] - 10, self.ship.pos[1] - 35))
        self.ship.screen.blit(distance_text, (self.ship.pos[0] - 10, self.ship.pos[1] - 50))
        self.ship.screen.blit(score_text, (self.ship.pos[0] - 10, self.ship.pos[1] - 65))
        