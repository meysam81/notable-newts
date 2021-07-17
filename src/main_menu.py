import os.path

from asciimatics.effects import Print
from asciimatics.exceptions import NextScene, StopApplication
from asciimatics.renderers import ColourImageFile, FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Layout

# constands
text_colour = Screen.COLOUR_WHITE


class MainMenuFrame(Frame):
    """
    Class that will show the main menu
    """

    def __init__(self, screen):
        """
        Here the frame with all layouts and widgets is created
        """
        # The settings for the frame in which the layouts are displayed
        super(MainMenuFrame, self).__init__(screen,
                                            screen.height,
                                            screen.width // 6,
                                            x=(screen.width * 5 // 12) + (screen.height * 5 // 12),
                                            y=screen.height//6 + 1,
                                            hover_focus=True,
                                            can_scroll=False,
                                            title="Contact Details",
                                            reduce_cpu=True,
                                            has_border=False)
        # The theme of the frame for every widget type (foreground, attribute, background)
        self.palette = {
            "background": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "borders": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "button": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "control": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "disabled": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "edit_text": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "field": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "focus_button": (text_colour, screen.A_BOLD, screen.COLOUR_BLACK),
            "focus_control": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "focus_edit_text": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "focus_field": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "invalid": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "label": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "scroll": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "selected_control": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "selected_field": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "selected_focus_control": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "selected_focus_field": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK),
            "title": (text_colour, screen.A_NORMAL, screen.COLOUR_BLACK)
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
        raise NextScene('game')

    def _levelSelect(self):
        """
        When the player chooses levels, display the level selection screen
        """
        raise NextScene('levelSelect')

    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")


class MainMenuScene(Scene):
    def __init__(self, screen: Screen):
        effects = [
            Print(screen,
                  FigletText("Think inside the box", font='big'),
                  x=(screen.width - 90) // 2,
                  y=0,
                  colour=text_colour),
            Print(screen,
                  ColourImageFile(screen,
                                  os.path.dirname(__file__) + '/../docs/images/game-avatar.png',
                                  screen.height*5//6,
                                  uni=screen.unicode_aware,
                                  dither=False),
                  x=0,
                  y=screen.height//6,
                  stop_frame=False),
            Print(screen,
                  FigletText("Notable\nNewts", font='small'),
                  x=screen.height * 9//12,
                  y=screen.height // 6 + int(screen.height * ((5/12) - (5*(1/7)/12))),
                  colour=text_colour)
        ]
        effects.append(MainMenuFrame(screen))
        duration = -1
        clear = True
        name = "mainMenu"
        super(MainMenuScene, self).__init__(
            effects,
            duration,
            clear,
            name
        )


if __name__ == "__main__":
    Screen.wrapper(MainMenuScene, catch_interrupt=True)
