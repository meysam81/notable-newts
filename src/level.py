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
        self.sqr_nr = 25
        self.screen = screen
        self.x_pad, self.y_pad = 2, 2
        self.x_sqr_sz, self.y_sqr_sz = 2, 1
        self.width, self.height = self.sqr_nr*self.x_sqr_sz + self.x_pad, self.sqr_nr*self.y_sqr_sz + self.y_pad

        self.player_x = (self.width)//2
        self.player_y = self.height - 1

        self.player_grid_x, self.player_grid_y = 11, 24

        self.path_taken: Tuple(int, int) = []
        self.grid: List[List[Tile]] = self.load_level()
        self.player = Player(self.player_x, self.player_y)

    def load_level(self) -> None:
        with open(config.general_settings.load_maze(2), "rb") as f:
            return pickle.load(f)

    def _draw_stage(self) -> None:
        """Draws static elements"""
        # THIS WILL BE REWORKED ALTOGETHER ONCE THE LEVEL MAKER IS IMPLEMENTED
        # the goal is to use self.grid to draw what is passable and what isn't
        _x, _y = self.x_pad, self.y_pad

        for row in self.grid:
            for col in row:
                if not col.passable:
                    self.screen.highlight(_x, _y, self.x_sqr_sz, self.y_sqr_sz, None, COLOUR_WHITE)
                else:
                    self.screen.highlight(_x, _y, self.x_sqr_sz, self.y_sqr_sz, None, COLOUR_GREEN)
                if col.enemy:
                    self.screen.highlight(_x, _y, self.x_sqr_sz, self.y_sqr_sz, None, COLOUR_RED)
                _x += self.x_sqr_sz
            _x = self.x_pad
            _y += self.y_sqr_sz

        # self.screen.move(self.x_pad, self.y_pad)
        # self.screen.draw(self.x_pad, self.y_pad + self.height, char="*")
        # self.screen.draw(self.x_pad + self.width, self.y_pad + self.height, char="*")
        # self.screen.draw(self.x_pad + self.width, self.y_pad, char="*")
        # self.screen.draw(self.x_pad, self.y_pad, char="*")

    def draw_path(self) -> None:
        for (x, y) in self.path_taken:
            self.screen.highlight(x, y, 1, 1, None, COLOUR_RED)

    def validate(self, m) -> bool:
        _future_x = self.player_grid_x + m[0]
        _future_y = self.player_grid_y + m[1]
        print(f"next: y:{_future_y}, x:{_future_x}")

        if _future_y > len(self.grid)-1 or _future_y > len(self.grid[0])-1:
            return False
        if _future_x < self.x_pad or _future_x + m[0] > self.width:
            return False
        if _future_y + m[1] < self.y_pad and _future_y + m[1] > self.height:
            return False
        if not self.grid[_future_y][_future_x].passable:
            return False
        return True

    def update_grid_pos(self, x, y):
        self.player_grid_x += x
        self.player_grid_y += y

    def run(self, moves: List[str]):
        self.screen.clear()
        while 1:
            for m in moves:
                self._draw_stage()

                if self.validate(m):
                    self.player.move((m[0]*self.x_sqr_sz, m[1]*self.y_sqr_sz))
                    self.update_grid_pos(m[0], m[1])

                bg = self.screen.get_from(self.player.x, self.player.y)[3]
                self.player.render(self.screen, bg)
                self.screen.refresh()
                self.screen.clear_buffer(0, 1, 0)
                sleep(0.2)
