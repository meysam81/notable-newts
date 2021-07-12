from asciimatics.effects import Print
from asciimatics.exceptions import StopApplication
from asciimatics.renderers import ColourImageFile, FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Layout

# constands
text_colour = Screen.COLOUR_WHITE


class mainMenuFrame(Frame):
    """
    Class that will show the main menu
    """

    def __init__(self, screen):
        """
        Here the frame with all layouts and widgets is created
        """
        # The settings for the frame in which the layouts are displayed
        super(mainMenuFrame, self).__init__(screen,
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


class mainMenuScene:
    def __init__(self, screen: Screen):
        effects = [
            Print(screen,
                  FigletText("Think inside the box", font='big'),
                  x=(screen.width - 90) // 2,
                  y=0,
                  colour=text_colour),
            Print(screen,
                  ColourImageFile(screen, "newt.png", screen.height*5//6,
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
        effects.append(mainMenuFrame(screen))
        self.scene = Scene(effects=effects, duration=-1, name="mainMenu")

    def getMenuScene(self):
        return self.scene
