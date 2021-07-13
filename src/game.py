from contextlib import suppress
from typing import Union

from asciimatics.event import Event, KeyboardEvent
from asciimatics.screen import Screen

from constants import ControlButtons, Directions
from level import Level


class Button:
    """A class representing a button"""

    def __init__(self, label: str, enum: int, selected: bool = False):
        self.label = label
        self.enum = enum

        self.selected = selected


class Game:
    """A class that represents the game"""

    def __init__(self):
        self.screen: Union[Screen, None] = None

    def _get_letter_from_code(self, key_code: int) -> str:
        """Return the key from the given key code returned by `KeyboardEvent.key_code`"""
        special_keys = {
            -204: Directions.UP,
            -206: Directions.DOWN,
            -203: Directions.LEFT,
            -205: Directions.RIGHT,
            -301: ControlButtons.TAB,
            -302: ControlButtons.BACK_TAB,
            13: ControlButtons.ENTER,
        }

        if key_code in special_keys:
            return special_keys[key_code]

        return chr(key_code).lower()

    def _get_active_button(self, buttons: list) -> Union[Button, None]:
        buttons = [button for button in buttons if button.selected]

        if buttons:
            return buttons[0]

    def _get_moves(self) -> list:
        """Gets the moves the player wants to input"""
        _buttons = [
            Button("Undo (u)", 0, True),
            Button("Reset (r)", 1),
            Button("Go (g)", 2),
        ]

        _moves = []

        while True:
            _rstart = (
                0
                if len(_moves) <= self.screen.height
                else len(_moves) - self.screen.height
            )

            for i, move in enumerate(_moves[_rstart:]):
                self.screen.print_at(move, 5, i)

            for i, button in enumerate(_buttons):

                self.screen.print_at(
                    button.label,
                    self.screen.width - (len(button.label) + 5),
                    i,
                    attr=Screen.A_REVERSE if button.selected else 0,
                )
            self.screen.refresh()
            self.screen.clear_buffer(0, 1, 0)

            event: Event = self.screen.get_event()

            if not event or not isinstance(event, KeyboardEvent):
                continue

            key = self._get_letter_from_code(event.key_code)

            if key == ControlButtons.ENTER:
                button = self._get_active_button(_buttons)

                if button:
                    button = button.enum

                    buttonmapping = {
                        0: "u",
                        1: "r",
                        2: "g",
                    }

                    key = buttonmapping[button]

            if key in list(Directions):
                _moves.append(key)

            elif key == "r":
                _moves = []

            elif key == "u":
                with suppress(IndexError):
                    _moves.pop()

            elif key == "g":
                break

            elif key == ControlButtons.TAB:
                button = self._get_active_button(_buttons)

                if button and _buttons.index(button) != len(_buttons) - 1:
                    _buttons[_buttons.index(button)].selected = False

                    _buttons[_buttons.index(button) + 1].selected = True

            elif key == ControlButtons.BACK_TAB:
                button = self._get_active_button(_buttons)

                if button and _buttons.index(button) != 0:
                    _buttons[_buttons.index(button)].selected = False

                    _buttons[_buttons.index(button) - 1].selected = True

        return _moves

    def run(self, screen: Screen) -> None:
        """Runs the game"""

        self.screen = screen
        moves = self._get_moves()
        l1 = Level(self.screen)
        l1.run(moves)
        print(moves)
