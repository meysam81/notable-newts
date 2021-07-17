from asciimatics.effects import Print
from asciimatics.exceptions import NextScene
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Layout

from custom_text_box import CustomTextBox
from level import Level

# constants
TEXT_COLOUR = Screen.COLOUR_WHITE


class GameFrame(Frame):
    """Game frame"""

    def __init__(self, screen: Screen):
        """Here the frame with the undo, reset and go button is created"""
        # The settings for the frame in which the layouts are displayed
        super(GameFrame, self).__init__(
            screen,
            screen.height,
            screen.width // 2,
            x=0,
            y=6,
            hover_focus=True,
            can_scroll=False,
            title="game",
            reduce_cpu=True,
            has_border=False,
            on_load=lambda: self.set_theme("monochrome")
        )

        layout = Layout([1, 1])
        self.add_layout(layout)
        layout.add_widget(Button("Go", self._go), 1)
        layout.add_widget(Button("Main Menu", self._main_menu), 1)
        self.input_field = CustomTextBox(screen.height-6, name='input')
        layout.add_widget(self.input_field, 0)
        self.fix()

    def _main_menu(self) -> None:
        raise NextScene("mainMenu")

    def _go(self) -> None:
        """Start the level simulator"""
        # TODO: add functionality
        level = Level(self.screen)
        level.run([x for x in self.input_field.value if x != ''])
        raise NextScene("endScreen")


class GameScene(Scene):
    """Game scene"""

    def __init__(self, screen: Screen):
        effects = [
            Print(screen,
                  FigletText("press w a s d to specify moves"),
                  x=0,
                  y=0,
                  colour=7),
            GameFrame(screen)]
        duration = -1
        clear = True
        name = "game"
        super(GameScene, self).__init__(
            effects,
            duration,
            clear,
            name
        )


if __name__ == "__main__":
    Screen.wrapper(GameScene, catch_interrupt=True)
