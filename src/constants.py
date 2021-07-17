from enum import Enum


# Inheriting from `str` because it makes string comparison possible
class BaseEnum(str, Enum):
    """Enum"""

    def __str__(self):
        return self.value


class Directions(BaseEnum):
    """Directions"""

    UP = "UP"
    RIGHT = "RIGHT"
    DOWN = "DOWN"
    LEFT = "LEFT"


class ControlButtons(BaseEnum):
    """Buttons"""

    TAB = "TAB"
    BACK_TAB = "BACK_TAB"
    ENTER = "ENTER"


class MenuBottons(BaseEnum):
    """Buttons"""

    UNDO = "UNDO"
    RESET = "RESET"
    GO = "GO"
