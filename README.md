# AI Piloted Lunar Lander

# check ins

**Wed, Jun 20th** 
Currently watching Tropic Thunder and absolutely crying laughing. Oh yeah, and I got the model trained and a working prediction loop up and running. Every 20 gameplay steps, each spaceship's agent calls model.predict() on the current telemetry data. The model is a dense feed forward network with 3 hidden layers with sizes from 256 to 64 to 32. During training, the model was stuck at around 65% accuracy, and an MSE loss of 0.1098 and it REFUSED to learn. After a few attempts, I was convinced that since the flight data it was trying to fit to was inherently random, I was probably never going to get a great fit, so I settled for just overfitting to around 200k timesteps of flight data. This assumption paid off, as moving onto the prediction loop, I found that the network actually flew quite well!



**Wed, Jun 18th** 

The scoring, telemetry, and basic agent classes are done! The Agent class uses the following basic heuristic rules to decide when to thrust and steer:

```
def fly(self):
    thrust = random.random() * 0.65 > self.ship.telemetry.altitude
    right = self.ship.telemetry.distance > 0.2 and random.random() < self.ship.telemetry.distance  * 0.3
    left = self.ship.telemetry.distance < -0.2 and random.random() < abs(self.ship.telemetry.distance)  * 0.3

    if (thrust): self.ship.thrust()
    if (right): self.ship.right()
    if (left): self.ship.left()
```

Next up is to collect the gameplay data, architect a basic dense neural network, and train it on the heuristic ruleset as a starting point. With the backbone model trained, I can then move onto a more complicated genetic algorithm to further improve the model.

Finally time for a screenshot. There are 10 ships at a time, each with it's telemetry data displayed overhead, with a text color corresponding to the score. Each value is ranged from either 0 to 1, or -1 to 1 to reduce the need for pre-processing in other classes.

![First Screenshot!](/public/images/first_screenshot.png)

*later that evening* I've got the DenseNetwork and Cache classes done! The cache class saves the telemetry data (altitude, velocity, and distance) and one hot encoded thrust, left, right actions, as a [state, action] pair for each timestep, and when each ship dies, it pickles it's flight data (just like a blackbox on a real aircraft!). 

The Cache class also has a load() method to load and flatten all flight-data files in the /data file as a list of shape (n, 2, 3) which can easily be split using numpy into x and y arrays for feeding into a keras.Sequential dense feed forward network.

As I write this entry, I'm running 100 games to collect a bunch of flight data, because my original dozen or so gameplay files didn't learn at all! In fact, the categorical crossentropy loss ballooned to over 150 in just 3 epochs! Oooooorrr maybe I'm just using the wrong loss function! We'll see, because it's gonna be a while before all 100 simulations finish. 

The current network is intentionally simple. I don't aim to immediately train a useful network, but instead to validate my training pipeline: fly, collect, train, repeat. At this point, all I need is a keras model that I can load and sample for real time flight decisions. To that end, the dense_model.py class below lacks a sample() method:

```
class DenseModel():
    def __init__(self):
        self.model = keras.Sequential([
            keras.layers.Input((3,)),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(32, activation='relu'),
            keras.layers.Dense(3, activation='softmax')
        ])
        self.model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=['accuracy'])
    
    def fit(self, flight_data):
        data = np.array(flight_data, dtype="float64")
        print(data.shape)
        x = data[:,0]
        y = data[:,1]
        self.model.fit(x, y, epochs=3, batch_size=32)
```

**Mon, Jun 16th**

I finished the basic game, it's an endless loop of 10 spaceships at a time falling towards a level surface. I also started with randomly generated terrain, but it doesn't work so good for collision detection, *but* it looks nice so I left it in.

I also abandoned rotating the craft. It's complicated both to code, and I assume to train the network, so we're pressing forward with just left to right motion. Next up are the landing zones, AI agents, and telemetry data collection.

*several hours and several episodes of Spongebob (season 3) later*  landing targets are started, 3 contentric shallow rectangles drawn around the horizontal center and just above the floor, in order of red, orange, green, from widest to narrowest.

I'm also starting to think that I want to turn this into a swarm controller, where each agent broadcasts info to and about other drones, including it's own position, vector distances to nearby drones, as well as velocities, angles, targets, and positive & negative feedback scores for getting too close, interfering with flight paths, etc.

# TODO
- (mostly done) Build the game
- (done) Spaceship
- (done) World
- (done) Game Loop
- (done) landing zone
- (done) heuristic agents
- AI agents
- (done) telemetry
- (done) cache
- (done) model
- (done) reward function
- (started) training
- let the model drive