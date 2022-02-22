import pygame
from pygame.locals import *

pygame.init()

SCREEN = pygame.display.set_mode((300,300))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
