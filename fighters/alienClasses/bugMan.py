from fighters import Fighters
from parts import Parts
from battleTypes import BattleType

class BugMan(Fighters):
    def __init__(self, selected):
        super().__init__(selected)
        self.shape = [[0,0],[0,1]]
        self.parts = [Parts(2, self.shape[0],"bug",4, BattleType.Air),
                      Parts(2, self.shape[1],"bug",4, BattleType.Air)]
    

    def returnParts(self):
        return self.parts
   