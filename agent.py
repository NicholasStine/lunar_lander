

import random
from cache import Cache
from dense_model import DenseModel

class Agent():
    def __init__(self, ship):
        self.ship = ship
        self.cache = Cache(ship)
        self.model = DenseModel(load_model='big_boy_brain_06_20')
        self.thrust = False
        self.right = False
        self.left = False
        self.steps_since_born = 0
    
    def fly(self, cache=False):
        altitude = self.ship.telemetry.altitude
        velocity = self.ship.telemetry.velocity
        distance = self.ship.telemetry.distance
        
        if self.steps_since_born % 5 == 0:
            thrust, right, left = 0, 0, 0
        if self.steps_since_born % 20 == 0:
            thrust, right, left = self.model.fly([altitude, velocity, distance])
            self.thrust = thrust
            self.right = right
            self.left = left
            # self.steps_since_born = 0
        # thrust = random.random() * 0.65 > self.ship.telemetry.altitude
        # right = self.ship.telemetry.distance > 0.2 and random.random() < self.ship.telemetry.distance  * 0.3
        # left = self.ship.telemetry.distance < -0.2 and random.random() < abs(self.ship.telemetry.distance)  * 0.3

        if (self.thrust): self.ship.thrust()
        if (self.right): self.ship.right()
        if (self.left): self.ship.left()
        
        if cache: self.cache.save([thrust, left, right])
        self.steps_since_born += 1
        return self.steps_since_born > 10000