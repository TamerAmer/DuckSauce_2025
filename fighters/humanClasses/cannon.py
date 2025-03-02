from fighters.fighters import Fighters
from ..parts import Parts
from battleTypes import BattleType
import pygame
import settings

class Cannon(Fighters):
    def __init__(self, selected, spritesheet):
        super().__init__(selected, spritesheet)
        pygame.sprite.Sprite.__init__(self)
        self.original_image = spritesheet.get_image_name("cannon")
        self.image = self.original_image  # Needed for proper rotation
        self.image = pygame.transform.scale(self.image,(settings.GRID_SPACE_SIZE * 2, settings.GRID_SPACE_SIZE * 1))
        self.rect = self.image.get_rect()
        self.shape = [(0,0),(0,1)]
        self.parts = [Parts(2, self.shape[0],"cannon",4, BattleType.Land),
                      Parts(2, self.shape[1],"cannon",4, BattleType.Land)]
    

    def returnParts(self):
        return self.parts