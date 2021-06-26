import ambiente
import individuo
import random as rn
import numpy as np
import pygame
from datetime import datetime



h, w = 1000, 1000
border = 5

am = ambiente.ambient()
am.try_resol()

pygame.init()
screen = pygame.display.set_mode((w + (2 * border), h + (2 * border)))
pygame.display.set_caption("Serious Work - not games")
done = False
clock = pygame.time.Clock()

# Get a font for rendering the frame number
basicfont = pygame.font.SysFont(None, 32)

# Clear screen to white before drawing
screen.fill((255, 255, 255))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Convert to a surface and splat onto screen offset by border width and height
    surface = pygame.surfarray.make_surface(am.display())

    surface = pygame.transform.scale(surface, (1000, 1000))
    screen.blit(surface, (border, border))


    pygame.display.flip()
    clock.tick(60)

    # current date and time
    now = datetime.now()

    am.try_resol()

    print((datetime.now() - now), "------------------")