import pygame

def checkRectCollision(rect_a, rect_b):
    collided = False
    for rect in rect_a.shapes:
        _collided = pygame.Rect.colliderect(rect, rect_b.shape)
        if _collided:
            collided = True
            break
    return collided