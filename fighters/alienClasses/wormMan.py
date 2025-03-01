from fighters.fighters import Fighters
from parts import Parts
from battleTypes import BattleType

class WormMan(Fighters):
    def __init__(self, selected, spritesheet):
        super().__init__(selected, spritesheet)
        self.original_image = spritesheet.get_image_name("wormman")
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.shape = [[0,0],[0,1],[0,2],[0,3]]
        self.parts = [Parts(2, self.shape[0],"worm",8, BattleType.AntiAir),
                      Parts(2, self.shape[1],"worm",8, BattleType.AntiAir), 
                      Parts(2, self.shape[2],"worm",8, BattleType.AntiAir), 
                      Parts(2, self.shape[3],"worm",8, BattleType.AntiAir)]
    
    def returnParts(self):
        return self.parts
     