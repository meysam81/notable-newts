class Tile:
    """The tiles that levels are based on"""
    def __init__(self, passable: bool = True, enemy: bool = False):
        # we could have different terrains like water to spice up the level design
        self.passable = passable
        self.enemy = enemy
