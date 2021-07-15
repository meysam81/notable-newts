from asciimatics.screen import Screen


class Player:
    """A class representing the player"""

    def __init__(self, x: int = 0, y: int = 0):
        """Initiates a player"""
        self.x = x
        self.y = y
        self.symbol = "o"

    def move(self, direction) -> None:
        """Moves the player"""
        self.x += direction[0]
        self.y += direction[1]

    def render(self, screen: Screen, bg) -> None:
        """Renders the player on the screen"""
        screen.print_at(self.symbol, self.x, self.y, bg=bg)
