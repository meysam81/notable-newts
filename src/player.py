# Import module
import sys
import time

# Import from asciimatics
import asciimatics
from asciimatics.event import KeyboardEvent
from asciimatics.screen import Screen


# Detect platform for type hints
if sys.platform == "win32":
    win_type = asciimatics.screen._WindowsScreen
else:
    win_type = asciimatics.screen._CursesScreen

# Constants
SPEED = 0.2


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

        # Player symbol
        self.symbol = "o"

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


def get_movement(screen: win_type) -> list:
    """Gets the moves from the player

    :arg screen: The screen to show the moves list on
    Uses get event to grab key inputs from the user and
    combines into a list
    """
    # Dictionary for key values and names of keys
    move_set = {-203: "L", -204: "U", -205: "R", -206: "D"}
    fancy_names = {"L": "Left", "U": "Up", "R": "Right", "D": "Down"}

    # List for key inputs
    movement = []

    # Loop for getting input keys
    while 1:
        # Get event
        event = screen.get_event()

        # If an event occurrs and it is a keyboard event
        if event is not None and type(event) == KeyboardEvent:

            # Quit if q pressed
            if event.key_code in (ord("q"), ord("Q")):
                return movement

            # Add movement if arrow keys pressed
            elif event.key_code in move_set:
                movement.append(move_set[event.key_code])

        # If list longer than screen, start later
        if len(movement) <= screen.height:
            start = 0
        else:
            start = len(movement)-screen.height

        # Show the inputs
        for i, move in enumerate(movement[start:]):
            screen.print_at(fancy_names[move], 1, i)

        # Show new movement and clear screen buffer after
        screen.refresh()
        screen.clear_buffer(0, 1, 0)


def game(screen: win_type) -> None:
    """Handles game

    :arg screen: The screen to draw to
    Performs the game loop
    """
    # Initialise player class
    player = Player()

    # Grab moves from player
    moves = get_movement(screen)

    # Game loop
    for j in range(len(moves)):
        # Move the player
        player.move(moves[j])

        # Show the player
        player.draw(screen)

        # Show on screen
        screen.refresh()
        screen.clear_buffer(0, 1, 0)

        time.sleep(SPEED)

    # Causes program to stay open until q key pressed
    while 1:
        event = screen.get_event()
        if event is not None and type(event) == KeyboardEvent and event.key_code in (ord("q"), ord("Q")):
            break

        time.sleep(0.5)


# Run screen
Screen.wrapper(game)
