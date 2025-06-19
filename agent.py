

import random


class Agent():
    def __init__(self, ship):
        self.ship = ship
    
    def fly(self):
        thrust = random.random() * 0.65 > self.ship.telemetry.altitude
        right = self.ship.telemetry.distance > 0.2 and random.random() < self.ship.telemetry.distance  * 0.3
        left = self.ship.telemetry.distance < -0.2 and random.random() < abs(self.ship.telemetry.distance)  * 0.3

        if (thrust): self.ship.thrust()
        if (right): self.ship.right()
        if (left): self.ship.left()
        