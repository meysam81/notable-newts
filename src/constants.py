from enum import Enum


class BaseEnum(str, Enum):
    def __str__(self):
        return self.value


class TupleEnum(tuple, Enum):
    def __str__(self):
        return str(self.value)


# Inheriting from `tuple` because it makes indexing possible
class Directions(TupleEnum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)


class ControlButtons(BaseEnum):
    TAB = "TAB"
    BACK_TAB = "BACK_TAB"
    ENTER = "ENTER"


class MenuBottons(BaseEnum):
    UNDO = "UNDO"
    RESET = "RESET"
    GO = "GO"
