

# I need to save and load gameplay in this class
# I need the input

# I need the score

import glob
import pickle
import time


class Cache():
    
    def __init__(self, ship):
        self.telemetry = ship.telemetry
        self.cache = []
    
    def pickle(self):
        with open(f'data/flight_{time.time()}.pkl', 'wb') as flight_file:
            pickle.dump(self.cache, flight_file)
        self.cache = []
    
    def save(self, action):
        step = [
            [self.telemetry.altitude, self.telemetry.velocity, self.telemetry.distance],
            [1.0 if action[0] else 0.0, 1.0 if action[1] else 0.0, 1.0 if action[2] else 0.0]
        ]
        self.cache.append(step)
    
    def load(self):
        games = []
        files = list(glob.glob('data/*.pkl'))
        for file in files:
            with open(file, 'rb') as flight_file:
                games += pickle.load(flight_file)
        return games