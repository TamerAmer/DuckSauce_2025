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
        self.gridAliens = []  # Tuples of alien objects and grid positions
        self.gridHumans = []

    def GenerateCoordinates(self):
        for y in range(self.rows):
            for x in range(self.columns):
                self.gridSpaceMetadata.append(GridSpace((x, y), None))

    def drawGrid(self, screen):
        for r in range(self.rows):
            for c in range(self.columns):
                pygame.draw.rect(screen, self.gridColour,
                                 [self.gridOffsetX + c * self.gridSpaceSize,
                                  self.gridOffsetZ + r * self.gridSpaceSize,
                                  self.gridSpaceSize, self.gridSpaceSize], 1)


    #def getAlienGridCoords(self, alien):
    #    self.gridHumans
    #    parts = alien.parts

    #    return alien_coords  # top left of the alien

    def checkAlienPlacement(self, alien, chosen_coords):
        print(chosen_coords)
        parts_list = alien.returnParts()
        placement_valid = True
        if chosen_coords is None:
            print("invalid")
            return False
        for p in parts_list:
            relative_x, relative_y = p.gridCo
            anchor_x, anchor_y = chosen_coords

            absolute_x = anchor_x + relative_x
            absolute_y = anchor_y + relative_y

            #print(f"abs {absolute_x}, {absolute_y}")
            # Check if alien parts are out of bound
            if absolute_x < 0 or absolute_x >= self.columns or absolute_y < 0 or absolute_y >= self.rows:
                placement_valid = False

            # Check if alien parts collide with other alien parts
            for i in self.gridSpaceMetadata:
                if i.alien_part is not None and i.coords == (absolute_x, absolute_y):
                    placement_valid = False
                    break

            if placement_valid == False:
                break

        print(placement_valid)
        return placement_valid

    def addAlien(self, alien, chosen_coords, human_or_alien):
        parts_list = alien.returnParts()
        if human_or_alien == 0:
            self.gridAliens.append((alien, chosen_coords))
        elif human_or_alien == 1:
            self.gridHumans.append((alien, chosen_coords))
        for p in parts_list:
            coords_x, coords_y = p.gridCo
            absolute_part_coords_x = coords_x + chosen_coords[0]
            absolute_part_coords_y = coords_y + chosen_coords[1]
            self.modifyGridSpace((absolute_part_coords_x, absolute_part_coords_y), p)
            #print(f"{absolute_part_coords_x} {absolute_part_coords_y}")


    def removeAlien(self, alien, chosen_coords, human_or_alien):
        parts_list = alien.returnParts()
        if human_or_alien == 0:
            self.gridAliens.append(alien)
        elif human_or_alien == 1:
            self.gridHumans.append(alien)
        self.gridAliens.remove(alien)
        for p in parts_list:
            coords_x, coords_y = p.gridCo
            absolute_part_coords_x = coords_x + chosen_coords[0]
            absolute_part_coords_y = coords_y + chosen_coords[1]
            self.modifyGridSpace((absolute_part_coords_x, absolute_part_coords_y), None)
            #print(f"{absolute_part_coords_x} {absolute_part_coords_y}")

    def getMouseGridCoords(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Convert to grid coordinates by subtracting offsets and dividing by cell size
        grid_x = (mouse_x - self.gridOffsetX) // self.gridSpaceSize
        grid_y = (mouse_y - self.gridOffsetZ) // self.gridSpaceSize

        # Ensure the coordinates are within grid bounds
        if 0 <= grid_x < self.columns and 0 <= grid_y < self.rows:
            #print(f"{grid_x}, {grid_y}")
            return grid_x, grid_y
        else:
            return None  # Mouse is outside the grid


    def modifyGridSpace(self, coords, alien_part):
        for i in self.gridSpaceMetadata:
            if i.coords == tuple(coords):
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