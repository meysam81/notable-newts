import sys

from asciimatics.effects import Print
from asciimatics.exceptions import ResizeScreenError, StopApplication
from asciimatics.renderers import ColourImageFile, FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Layout

import config

# constants
TEXT_COLOUR = Screen.COLOUR_WHITE


class MainMenuFrame(Frame):
    """
    Class that will show the main menu
    """

    def __init__(self, screen):
        """
        Here the frame with all layouts and widgets is created
        """
        # The settings for the frame in which the layouts are displayed
        super(MainMenuFrame, self).__init__(
            screen,
            screen.height,
            screen.width // 6,
            x=(screen.width * 5 // 12) + (screen.height * 5 // 12),
            y=screen.height // 6 + 1,
            hover_focus=True,
            can_scroll=False,
            title="Contact Details",
            reduce_cpu=True,
            has_border=False,
        )
        # The theme of the frame for every widget type (foreground, attribute, background)
        self.palette = {
            "background": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "borders": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "button": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "control": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "disabled": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "edit_text": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "field": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "focus_button": (TEXT_COLOUR, screen.A_BOLD, screen.COLOUR_BLACK),
            "focus_control": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "focus_edit_text": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "focus_field": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "invalid": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "label": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "scroll": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "selected_control": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "selected_field": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "selected_focus_control": (
                TEXT_COLOUR,
                screen.A_NORMAL,
                screen.COLOUR_BLACK,
            ),
            "selected_focus_field": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
            "title": (TEXT_COLOUR, screen.A_NORMAL, screen.COLOUR_BLACK),
        }
        # The layouts will will be displayed in the frame
        layout1 = Layout([1])
        layout2 = Layout([1])
        layout3 = Layout([1])
        self.add_layout(layout1)
        self.add_layout(layout2)
        self.add_layout(layout3)
        # The widgets which will be displayed in the layouts
        layout1.add_widget(Button("Play", self._play), 0)
        layout2.add_widget(Button("Levels", self._levelSelect), 0)
        layout3.add_widget(Button("Exit", self._quit), 0)
        self.fix()

    def _play(self):
        """
        When the player chooses play, start the game
        """
        # TODO: start game
        pass

    def _levelSelect(self):
        """
        When the player chooses levels, display the level selection screen
        """
        # TODO: Show level select screen
        pass

    @staticmethod
    def _quit():
        # Close program
        raise StopApplication("User pressed quit")


def main_menu_effects(screen):
    """
    Get the effects for the main menu. This is the game name, logo and team name.
    """
    effects = [
        Print(
            screen,
            FigletText("Think inside the box", font="big"),
            x=(screen.width - 90) // 2,
            y=0,
            colour=TEXT_COLOUR,
        ),
        Print(
            screen,
            ColourImageFile(
                screen,
                config.general_settings.GAME_LOGO_PATH,
                screen.height * 5 // 6,
                uni=screen.unicode_aware,
                dither=False,
            ),
            x=0,
            y=screen.height // 6,
            stop_frame=False,
        ),
        Print(
            screen,
            FigletText("Notable\nNewts", font="small"),
            x=screen.height * 9 // 12,
            y=screen.height // 6 + int(screen.height * ((5 / 12) - (5 * (1 / 7) / 12))),
            colour=TEXT_COLOUR,
        ),
    ]
    return effects


def start_main_menu(screen):
    """
    Start up the main menu screen
    """
    effects = main_menu_effects(screen)
    effects.append(MainMenuFrame(screen))
    scenes = [Scene(effects=effects, duration=-1, name="Main")]
    screen.play(scenes, stop_on_resize=True, allow_int=True)


while True:
    try:
        Screen.wrapper(start_main_menu, catch_interrupt=True)
        sys.exit(0)
    except ResizeScreenError:
        pass
