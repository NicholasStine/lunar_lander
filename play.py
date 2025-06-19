import pygame
from collisions import checkRectCollision
from spaceship import Spaceship
from world import World

SCREEN_SIZE = (900,900)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
world = World(screen)
thrust = False
left = False
right = False
while True:
    spaceships = [Spaceship(screen, world) for _ in range(10)]
    world.generateTerrain()
    world.generateLandingZones()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    thrust = True
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_UP):
                    thrust = False
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False

        screen.fill((0, 0, 0))
        world.update()
        for spaceship in spaceships:
            spaceship.agent.fly()
            if thrust: spaceship.thrust()
            if left: spaceship.left()
            if right: spaceship.right()
            spaceship.update()
            collided = checkRectCollision(world, spaceship)
            if collided: spaceship.die()

        spaceships = list(filter(lambda ship: ship.dead == False, spaceships))
        if not len(spaceships): break
        pygame.display.flip()