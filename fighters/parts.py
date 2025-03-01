from battleTypes import BattleType

class Parts():
    def __init__(self, hp, gridCo, parent, totalHp, battleType:BattleType):
        self.hp = hp
        self.gridCo = gridCo
        self.parent = parent
        self.totalHp = totalHp
        self.BattleType = battleType
