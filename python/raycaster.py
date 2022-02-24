#Imports
import pygame
import pygame.gfxdraw
from pygame.locals import *

from maps import setWorld


#Colors
C_BLACK = pygame.Color(0, 0, 0)
C_WHITE = pygame.Color(255, 255, 255)
C_GREY  = pygame.Color(150, 150, 150)
C_RED   = pygame.Color(200, 100, 100)
C_GREEN = pygame.Color(100, 200, 100)


#Window Init
zoom = 3
pygame.init()
pygame.display.set_caption('Raycaster')
SCREEN = pygame.display.set_mode((128*zoom,128*zoom))


#Graphical Functions
def draw():
    SCREEN.fill(C_BLACK)
    minimap()
    pygame.display.update()

def pixel(x, y, color):
    for i in range (zoom):
        for j in range (zoom):
            pygame.gfxdraw.pixel(SCREEN, x*zoom+i, y*zoom+j, color)


#Entities
class Entity:
    def __init__(self, Type, Id, x, y, speed, angle, rotationSpeed):
        self.Type = Type
        # Type = 0: player
        # Type = 1: ennemy
        self.Id = Id
        #Id: The id of the entity in the list of entities of the current level
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.rotationSpeed = rotationSpeed

entities = []

def createEntity(Type, x, y, speed, angle, rotationSpeed):
    entities.append(Entity(Type, len(entities), x, y, speed, angle, rotationSpeed))
    


#Minimap
def minimap():
    for y in range (world.height):
        for x in range (world.width):
            if world.Map[y][x] == 1:
                pixel(x, y, C_GREY)
            elif world.Map[y][x] == 0:
                pixel(x, y, C_WHITE)
    for i in range(len(entities)): #Drawing every entity of the current level
        if entities[i].Type == 0: #Player
            pixel(entities[i].x, entities[i].y, C_GREEN)
        elif entities[i].Type == 1: #Ennemy
            pixel(entities[i].x, entities[i].y, C_RED)


#Game Init
world = setWorld(0)
createEntity(0, 1, 1, 0.1, 0, 0.02) #Adding the player
createEntity(1, 3, 3, 2, 2, 2) #Adding an ennemy
print(entities[0])


#Game loop
while True:
    entities[0] = player
    draw()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
