from aliens import Alien
from parts import Parts

class CrabMan(Alien):
    def __init__(self, selected):
        super().__init__(selected)
        self.shape = [[0,0],[0,1],[0,2],[0,3]]
    
    def returnParts(self):
        wormParts = []
        for crabGrid in self.shape:
            wormParts.append(Parts(1, crabGrid,"wormMan"))
        return wormParts
     