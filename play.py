import pygame
from collisions import checkRectCollision
from dense_model import DenseModel
from joystick import Joystick
from spaceship import Spaceship
from world import World

SPACESHIP_COUNT = 3
SCREEN_SIZE = (900,900)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

world = World(screen)
joystick = Joystick()

thrust = False
left = False
right = False
spaceships = [Spaceship(screen, world) for _ in range(SPACESHIP_COUNT)]

for game_i in range(10):
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
                print(spaceship.telemetry.score)
                spaceship.die()

        spaceships = list(filter(lambda ship: ship.dead == False, spaceships))
        if not len(spaceships): break
        pygame.display.flip()
        step_i += 1
    spaceships = [Spaceship(screen, world) for _ in range(SPACESHIP_COUNT)]
