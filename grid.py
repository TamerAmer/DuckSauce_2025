import pygame

class Grid():
    def __init__(self, rows, columns, gridSpaceSize, gridColour, gridOffsetX, gridOffsetZ):
        self.rows = rows
        self.columns = columns
        self.gridSpaceMetadata = []
        self.gridSpaceSize = gridSpaceSize
        self.gridColour = gridColour
        self.gridOffsetX = gridOffsetX
        self.gridOffsetZ = gridOffsetZ

    def GenerateCoordinates(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.gridSpaceMetadata.append(GridSpace((x, y), None))

    def DrawGrid(self, screen):
        for r in range(self.rows):
            for c in range(self.columns):
                pygame.draw.rect(screen, self.gridColour,
                                 [self.gridOffsetX + c * self.gridSpaceSize,
                                  self.gridOffsetZ + r * self.gridSpaceSize,
                                  self.gridSpaceSize, self.gridSpaceSize], 1)

    #def CheckMobPlacement(self, mob):
    #    partsList = mob.Parts
    #    for p in PartsList:




# GridSpace is the element of a grid. It has grid coordinates and mobPart for the info of monsters
class GridSpace():
    def __init__(self, coords, mobPart):
        self.coords = coords
        self.mobPart = mobPart

    def getCoordX(self):
        return self.coords(0)

    def getCoordY(self):
        return self.coords(1)

    def getMobPart(self):
        return self.mobPart





