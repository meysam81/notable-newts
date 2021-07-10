# Import from modules
import time

from asciimatics.screen import Screen

# Player class
class Player:
    def __init__(self):
        # Player coordinates
        self.x = 0
        self.y = 0
        self.symbol = "."

    def move(self, direction):
        # Each movement direction
        if direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1
        elif direction == "U":
            self.y -= 1
        elif direction == "D":
            self.y += 1

    def draw(self, screen):
        # Draw player to screen
        screen.print_at(self.symbol, self.x, self.y)


def demo(screen):
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
Screen.wrapper(demo)
