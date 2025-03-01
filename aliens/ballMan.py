from aliens import Alien
from parts import Parts
from battleTypes import BattleType

class BallMan(Alien):
    def __init__(self, selected):
        super().__init__(selected)
        self.shape = [[0,0]]
        self.parts = [Parts(2, self.shape[0],"ball", 2 , BattleType.Land)]

    def returnParts(self):
        return self.parts
     