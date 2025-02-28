from aliens import Alien
from parts import Parts

class CrabMan(Alien):
    def __init__(self, selected):
        super().__init__(selected)
        self.shape = [[0,0],[0,1],[1,1],[1,0]]
    
    def returnParts(self):
        crabParts = []
        for crabGrid in self.shape:
            crabParts.append(Parts(1, crabGrid,"crab"))
        return crabParts
     
    
