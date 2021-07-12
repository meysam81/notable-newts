from time import sleep
from typing import Any, List, Tuple

from asciimatics.constants import COLOUR_RED
from asciimatics.screen import Screen

from player import Player


class Tile:
    """The tiles that levels are based on"""

    def __init__(self, passable: bool = True, enemy: bool = False, terrain: Any = None):
        # we could have different terrains like water to spice up the level design
        self.passable = passable
        self.enemy = enemy
        self.terrain = terrain


class Level:
    """Framework for levels"""

    def __init__(self, screen: Screen):
        """Initiates a level"""
        self.screen = screen
        self.width, self.height = 70, 30
        self.x_pad, self.y_pad = 30, 5
        self.player_x = self.width // 2 + self.x_pad
        self.player_y = self.height - 1 + self.y_pad

        self.path_taken: Tuple(int, int) = []
        self.grid = [[Tile() for _ in range(self.width)] for __ in range(self.height)]
        self.player = Player(self.player_x, self.player_y)

    def _draw_stage(self) -> None:
        """Draws static elements"""
        # THIS WILL BE REWORKED ALTOGETHER ONCE THE LEVEL MAKER IS IMPLEMENTED
        # the goal is to use self.grid to draw what is passable and what isn't
        self.screen.move(self.x_pad, self.y_pad)
        self.screen.draw(self.x_pad, self.y_pad + self.height, char="*")
        self.screen.draw(self.x_pad + self.width, self.y_pad + self.height, char="*")
        self.screen.draw(self.x_pad + self.width, self.y_pad, char="*")
        self.screen.draw(self.x_pad, self.y_pad, char="*")

    def draw_path(self) -> None:
        for (x, y) in self.path_taken:
            self.screen.highlight(x, y, 1, 1, None, COLOUR_RED)

    def run(self, moves: List[str]):
        self.screen.clear()

        for m in moves:
            self._draw_stage()

            self.player.move(m)
            self.player.render(self.screen)
            self.draw_path()

            self.screen.refresh()
            self.screen.clear_buffer(0, 1, 0)
            self.path_taken.append((self.player.x, self.player.y))
            sleep(0.2)
