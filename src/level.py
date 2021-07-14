import pickle
from time import sleep
from typing import List, Tuple

from asciimatics.constants import COLOUR_GREEN, COLOUR_RED, COLOUR_WHITE
from asciimatics.screen import Screen

import config
from player import Player
from tile import Tile


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
        self.grid: List[List[Tile]] = self.load_level()
        self.player = Player(self.player_x, self.player_y)

    def load_level(self) -> None:
        with open(config.general_settings.load_maze(0), "rb") as f:
            return pickle.load(f)

    def _draw_stage(self) -> None:
        """Draws static elements"""
        # THIS WILL BE REWORKED ALTOGETHER ONCE THE LEVEL MAKER IS IMPLEMENTED
        # the goal is to use self.grid to draw what is passable and what isn't
        _x, _y = self.x_pad, self.y_pad
        _x_s, _y_s = 1, 1
        for row in self.grid:
            for col in row:
                if not col.passable:
                    self.screen.highlight(_x, _y, 1, 1, None, COLOUR_WHITE)
                else:
                    self.screen.highlight(_x, _y, 1, 1, None, COLOUR_GREEN)
                if col.enemy:
                    self.screen.highlight(_x, _y, 1, 1, None, COLOUR_RED)
                _x += _x_s
            _x = self.x_pad
            _y += _y_s

        # self.screen.move(self.x_pad, self.y_pad)
        # self.screen.draw(self.x_pad, self.y_pad + self.height, char="*")
        # self.screen.draw(self.x_pad + self.width, self.y_pad + self.height, char="*")
        # self.screen.draw(self.x_pad + self.width, self.y_pad, char="*")
        # self.screen.draw(self.x_pad, self.y_pad, char="*")

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
