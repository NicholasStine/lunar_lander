# AI Piloted Lunar Lander

# check ins
Mon, Jun 16th
I finished the basic game, it's an endless loop of 10 spaceships at a time falling towards a level surface. I also started with randomly generated terrain, but it doesn't work so good for collision detection, *but* it looks nice so I left it in.

I also abandoned rotating the craft. It's complicated both to code, and I assume to train the network, so we're pressing forward with just left to right motion. Next up are the landing zones, AI agents, and telemetry data collection.

*several hours and several episodes of Spongebob (season 3) later*  landing targets are started, 3 contentric shallow rectangles drawn around the horizontal center and just above the floor, in order of red, orange, green, from widest to narrowest.

I'm also starting to think that I want to turn this into a swarm controller, where each agent broadcasts info to and about other drones, including it's own position, vector distances to nearby drones, as well as velocities, angles, targets, and positive & negative feedback scores for getting too close, interfering with flight paths, etc.

# TODO
- (mostly done) Build the game
- (done) Spaceship
- (done) World
- (done) Game Loop
- landing zone
- agents (autonymous pilots)
- telemetry

- today I want to get a basic game loop, with a rectangle that falls to the ground.
  *note to self mon jun 16, I finished this the day after I started the project.