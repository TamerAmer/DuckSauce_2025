from fighters import Fighters
from parts import Parts
from battleTypes import BattleType
import pygame

class CrabMan(Fighters):
    def __init__(self, selected, spritesheet):
        super().init(selected, spritesheet)
        pygame.sprite.Sprite.init(self)
        self.original_image = spritesheet.get_image_name("crabman_00")
        self.image = self.original_image  # Needed for proper rotation
        self.rect = self.image.get_rect()
        self.shape = [[0,0],[0,1],[1,1],[1,0]]
        self.parts = [Parts(2, self.shape[0],"crab",8, BattleType.Land),
                      Parts(2, self.shape[1],"crab",8, BattleType.Land), 
                      Parts(2, self.shape[2],"crab",8, BattleType.Land), 
                      Parts(2, self.shape[3],"crab",8, BattleType.Land)]
    

    def returnParts(self):
        return self.parts
   