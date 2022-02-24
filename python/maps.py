#Creating a world class
class world:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.Map = [[0 for x in range(width)] for y in range(height)]


#Creating the levels
    #Test Level
worldTest = world(10, 8)
for y in range (8):
    for x in range (10):
        worldTest.Map[y][x] = 1
for y in range (1, worldTest.height-1):
    for x in range (1, worldTest.width-1):
        worldTest.Map[y][x] = 0


#Functions
def setWorld(Id):
    if Id == 0:
        return (worldTest)