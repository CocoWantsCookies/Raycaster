import pygame
from pygame.locals import *

import maps

pygame.init()

SCREEN = pygame.display.set_mode((256,224))
pygame.display.set_caption('Raycaster')

C_WHITE= pygame.Color(255, 255, 255)

pygame.display.update()

# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
