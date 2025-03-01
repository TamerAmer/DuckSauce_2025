from fighters.fighters import Fighters
from parts import Parts
from battleTypes import BattleType
import pygame

class Soldier(Fighters):
    def __init__(self, selected, spritesheet):
        super().init(selected, spritesheet)
        pygame.sprite.Sprite.init(self)
        self.original_image = spritesheet.get_image_name("soldier")
        self.image = self.original_image  # Needed for proper rotation
        self.rect = self.image.get_rect()
        self.shape = [[0,0]]
        self.parts = [Parts(2, self.shape[0],"soldier",2, BattleType.Land)]
    

    def returnParts(self):
        return self.parts
   