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

    def drawGrid(self, screen):
        for r in range(self.rows):
            for c in range(self.columns):
                pygame.draw.rect(screen, self.gridColour,
                                 [self.gridOffsetX + c * self.gridSpaceSize,
                                  self.gridOffsetZ + r * self.gridSpaceSize,
                                  self.gridSpaceSize, self.gridSpaceSize], 1)

    def checkAlienPlacement(self, alien, chosen_coords):
        parts_list = alien.returnParts()
        placement_valid = True
        for p in parts_list:
            coords = p.gridCo
            absolute_part_coords = coords + chosen_coords

            # Check if alien parts are out of bound
            if (absolute_part_coords < 0) or (absolute_part_coords > self.columns) or (absolute_part_coords < 0) or (absolute_part_coords > self.rows):
                placement_valid = False

            # Check if alien parts collide with other alien parts
            for i in self.gridSpaceMetadata:
                if (i.alien_part != None):
                    if (i.coords == absolute_part_coords):
                        placement_valid = False

        return placement_valid

    def addAlien(self, alien, chosen_coords):
        parts_list = alien.returnParts()
        for p in parts_list:
            coords = p.gridCo
            absolute_part_coords = coords + chosen_coords
            self.ModifyGridSpace(absolute_part_coords, p)

    def getMouseGridCoords(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Convert to grid coordinates by subtracting offsets and dividing by cell size
        grid_x = (mouse_x - self.gridOffsetX) // self.gridSpaceSize
        grid_y = (mouse_y - self.gridOffsetZ) // self.gridSpaceSize

        # Ensure the coordinates are within grid bounds
        if 0 <= grid_x < self.columns and 0 <= grid_y < self.rows:
            print(f"{grid_x}, {grid_y}")
            return grid_x, grid_y
        else:
            return None  # Mouse is outside the grid


    def modifyGridSpace(self, coords, alien_part):
        for i in self.gridSpaceMetadata:
            if i.coords() == coords:
                i.alien_part = alien_part


# GridSpace is the element of a grid. It has grid coordinates and mobPart for the info of monsters
class GridSpace():
    def __init__(self, coords, alien_part):
        self.coords = coords
        self.alien_part = alien_part

    def getCoordX(self):
        return self.coords(0)

    def getCoordY(self):
        return self.coords(1)

    def getMobPart(self):
        return self.alien_part





