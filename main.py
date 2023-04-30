import pygame
import sys

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Meteor Shooter")

# importing images
ship_surface = pygame.image.load('./graphics/ship.png')
# test_surf = pygame.Surface((400, 100))

while True:
    # input -> events (click, movement, buttons, controls)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # updates  ----------------------x--y
    display_surface.fill((0, 0, 0))
    display_surface.blit(ship_surface, (300, 500))
    # show frames to player
    pygame.display.update()
