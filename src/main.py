from asciimatics.screen import Screen

from game import Game

if __name__ == "__main__":
    game = Game()

    Screen.wrapper(game.run)
