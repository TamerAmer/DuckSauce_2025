from battleTypes import BattleType

class Parts():
    def __init__(self, gridCo, hp, parent, totalHp, battleType:BattleType):
        self.hp = hp
        self.gridCo = gridCo
        self.parent = parent
        self.totalHp = totalHp
        self.BattleType = battleType
