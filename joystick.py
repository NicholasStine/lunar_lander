import pygame

class Joystick():
    def __init__(self):
        pass
    
    def fly(self, event):
        thrust = False
        left = False
        right = False
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
        return thrust, left, right