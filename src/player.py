from asciimatics.screen import Screen

from constants import Directions


class Player:
    """A class representing the player"""

    def __init__(self, x: int = 0, y: int = 0):
        """Initiates a player"""
        self.x = x
        self.y = y
        self.symbol = "o"

    def move(self, direction: str) -> None:
        """Moves the player"""
        direction = direction.upper()

        if direction == Directions.UP:
            self.y -= 1
        elif direction == Directions.DOWN:
            self.y += 1
        elif direction == Directions.LEFT:
            self.x -= 1
        elif direction == Directions.RIGHT:
            self.x += 1

    def render(self, screen: Screen) -> None:
        """Renders the player on the screen"""
        screen.print_at(self.symbol, self.x, self.y)
