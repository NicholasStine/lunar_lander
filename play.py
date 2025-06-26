import pygame
from collisions import checkRectCollision
from dense_model import DenseModel
from genetic_algo import sexytimes
from joystick import Joystick
from spaceship import Spaceship
from world import World

SPACESHIP_COUNT = 8
SCREEN_SIZE = (900,900)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

world = World(screen)
joystick = Joystick()

thrust = False
left = False
right = False
spaceships = [Spaceship(screen, world) for _ in range(SPACESHIP_COUNT)]
deadships = []

for game_i in range(100):
    world.generateTerrain()
    world.generateLandingZones()
    step_i = 0
    while True:
        # if step_i > 500: break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            thrust, left, right = joystick.fly(event)

        screen.fill((0, 0, 0))
        world.update()
        for spaceship in spaceships:
            die = spaceship.agent.fly()
            
            if thrust: spaceship.thrust()
            if left: spaceship.left()
            if right: spaceship.right()
            spaceship.update()
            collided = checkRectCollision(world, spaceship)
            if collided or die: 
            # if collided:
                # print(spaceship.telemetry.score)
                deadships.append(spaceship.die())

        spaceships = list(filter(lambda ship: ship.dead == False, spaceships))
        if not len(spaceships): break
        pygame.display.flip()
        step_i += 1
    
    spacecadets = []
    deadships = sorted(deadships, key=lambda ship: ship.telemetry.score)
    deadships = deadships[len(deadships) // 2:]
    for ship in deadships:
        print(ship.telemetry.score)
    for parents in zip(deadships[::2], deadships[1::2]):
        children = [*sexytimes(*parents), *sexytimes(*parents)]
        print(len(children))
        spacecadets.extend(children)
    spaceships = spacecadets
    deadships = []
