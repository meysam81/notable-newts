# Import module
import time
import sys

import asciimatics
from asciimatics.screen import Screen

if sys.platform == "win32":
    win_type = asciimatics.screen._WindowsScreen
else:
    win_type = asciimatics.screen._CursesScreen


# Player class
class Player:
    """A class for the player"""

    def __init__(self):
        """Init method for the player

        Stores the coordinates and player symbol
        """
        # Player coordinates
        self.x = 0
        self.y = 0
        self.symbol = "."

    def move(self, direction: str) -> None:
        """Handles movement

        :arg direction: The direction for the player to move
        Changes the players coordinates depending
        on the given direction
        """
        # Each movement direction
        if direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1
        elif direction == "U":
            self.y -= 1
        elif direction == "D":
            self.y += 1

    def draw(self, screen: win_type) -> None:
        """Handles drawing player

        :arg screen: The screen to draw the player to
        Shows the player on the screen at the stored coordinates
        """
        # Draw player to screen
        screen.print_at(self.symbol, self.x, self.y)


def game(screen: win_type) -> None:
    """Handles game

    :arg screen: The screen to draw to
    Performs the game loop
    """
    # Initialise player class
    player = Player()

    # Variable to keep track of place in movement list
    j = 0

    # Game loop
    while 1:
        # Move the player
        player.move(movement[j])

        # Show the player
        player.draw(screen)

        # Get keys pressed and quit if q pressed
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return

        # Update place in list
        j += 1
        j %= 4

        # Show changes in screen
        screen.refresh()

        # Clear screen
        screen.clear_buffer(0, 1, 0)

        # Wait for next loop
        time.sleep(0.5)


# Movement list
movement = ["D", "R", "L", "U"]

# Run screen
Screen.wrapper(game)
