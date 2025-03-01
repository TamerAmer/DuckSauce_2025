from fighters.fighters import Fighters
from parts import Parts
from battleTypes import BattleType
import pygame

class WaspMan(Fighters):
    def __init__(self, selected, spritesheet):
        super().__init__(selected, spritesheet)
        pygame.sprite.Sprite.__init__(self)
        self.original_image = spritesheet.get_image_name("waspman")
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.shape = [[0,0],[0,1],[1,1]]
        self.parts = [Parts(2, self.shape[0],"wasp",6, BattleType.Air),
                      Parts(2, self.shape[1],"wasp",6, BattleType.Air), 
                      Parts(2, self.shape[2],"wasp",6, BattleType.Air)]

    

    def returnParts(self):
        return self.parts
   