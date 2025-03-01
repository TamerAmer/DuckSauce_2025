from fighters import Fighters
from parts import Parts
from battleTypes import BattleType

class WormMan(Fighters):
    def __init__(self, selected):
        super().__init__(selected)
        self.shape = [[0,0],[0,1],[0,2],[0,3]]
        self.parts = [Parts(2, self.shape[0],"worm",8, BattleType.AntiAir),
                      Parts(2, self.shape[1],"worm",8, BattleType.AntiAir), 
                      Parts(2, self.shape[2],"worm",8, BattleType.AntiAir), 
                      Parts(2, self.shape[3],"worm",8, BattleType.AntiAir)]
    
    def returnParts(self):
        return self.parts
     