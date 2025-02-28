from aliens import Alien
from parts import Parts

class BallMan(Alien):
    def __init__(self, selected):
        super().__init__(selected)
        self.shape = [[0,0]]
    
    def returnParts(self):
        ballParts = []
        for crabGrid in self.shape:
            ballParts.append(Parts(1, crabGrid,"ballMan"))
        return ballParts
     