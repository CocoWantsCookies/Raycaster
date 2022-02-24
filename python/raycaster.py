#Imports
import pygame
import pygame.gfxdraw
from pygame.locals import *

from maps import setWorld


#Colors
C_BLACK= pygame.Color(0, 0, 0)
C_WHITE= pygame.Color(255, 255, 255)
C_GREY= pygame.Color(150, 150, 150)


#Window Init
zoom = 3
pygame.init()
pygame.display.set_caption('Raycaster')
SCREEN = pygame.display.set_mode((128*zoom,128*zoom))


#Functions
def draw():
    SCREEN.fill(C_BLACK)
    minimap()
    pygame.display.update()

def pixel(x, y, color):
    for i in range (zoom):
        for j in range (zoom):
            pygame.gfxdraw.pixel(SCREEN, x*zoom+i, y*zoom+j, color)

def minimap():
    for y in range (world.height):
        for x in range (world.width):
            if world.Map[y][x] == 1:
                pixel(x, y, C_GREY)
            elif world.Map[y][x] == 0:
                pixel(x, y, C_WHITE)


#Game Init
world = setWorld(0)


#Game loop
while True:
    draw()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
