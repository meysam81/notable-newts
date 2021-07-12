from enum import Enum


class BaseEnum(str, Enum):
    def __str__(self):
        return self.value


# Inheriting from `str` because it makes string comparison possible
class Directions(BaseEnum):
    UP = "UP"
    RIGHT = "RIGHT"
    DOWN = "DOWN"
    LEFT = "LEFT"


class ControlButtons(BaseEnum):
    TAB = "TAB"
    BACK_TAB = "BACK_TAB"
    ENTER = "ENTER"


class MenuBottons(BaseEnum):
    UNDO = "UNDO"
    RESET = "RESET"
    GO = "GO"
