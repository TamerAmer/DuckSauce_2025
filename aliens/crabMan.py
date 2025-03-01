import settings
from aliens.aliens import Alien
#from parts import Parts
import pygame


class CrabMan(Alien):
    def __init__(self, selected, spritesheet, x, y):
        super().__init__(selected, spritesheet, x, y)
        pygame.sprite.Sprite.__init__(self)
        self.original_image = spritesheet.get_image_name("crabman")
        self.image = self.original_image  # Needed for proper rotation
        self.image = pygame.transform.scale(self.image, (settings.GRID_SPACE_SIZE * 2, settings.GRID_SPACE_SIZE * 2))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.shape = [[0,0],[0,1],[1,1],[1,0]]
        self.x = x
        self.y = y
    
    #def returnParts(self):
    #    crabParts = []
    #    for crabGrid in self.shape:
    #        crabParts.append(Parts(1, crabGrid,"crab"))
    #    return crabParts
     
    
