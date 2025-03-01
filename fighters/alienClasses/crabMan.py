from fighters.fighters import Fighters
from parts import Parts
from battleTypes import BattleType

class CrabMan(Fighters):
    def __init__(self, selected):
        super().__init__(selected)
        self.shape = [[0,0],[0,1],[1,1],[1,0]]
        self.parts = [Parts(2, self.shape[0],"crab",8, BattleType.Land),
                      Parts(2, self.shape[1],"crab",8, BattleType.Land), 
                      Parts(2, self.shape[2],"crab",8, BattleType.Land), 
                      Parts(2, self.shape[3],"crab",8, BattleType.Land)]
    

    def returnParts(self):
        return self.parts
   