from asciimatics.effects import Print
from asciimatics.exceptions import NextScene
from asciimatics.renderers import Box, FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Label, Layout

TEXT_COLOUR = Screen.COLOUR_WHITE


class EndScreen(Frame):
    """Framework for end screen"""

    def __init__(self, state: bool, screen: Screen, time: float, x_pad: int, win_width: int, y_pad: int, height: int):
        """Initiates end screen"""
        self.text_width = 60
        self.x_pos, self.y_pos = x_pad + (win_width - self.text_width)//2, y_pad + height - 5
        super(EndScreen, self).__init__(
            screen,
            3,
            self.text_width,
            x=self.x_pos,
            y=self.y_pos,
            hover_focus=True,
            can_scroll=False,
            title="Contact Details",
            reduce_cpu=True,
            has_border=False,
            on_load=lambda: self.set_theme("monochrome")
        )

        self.state = state
        self.time = time

        layout1 = Layout([1])
        blank = Layout([1])
        layout2 = Layout([1, 1, 1])

        self.add_layout(layout1)
        self.add_layout(blank)
        self.add_layout(layout2)

        text = ""
        if state:
            text = f"You finished in time: {time}s"

        layout1.add_widget(Label(text, align="^"), 0)

        blank.add_widget(Label(""), 0)

        layout2.add_widget(Button("Next Level", self._next), 0)
        layout2.add_widget(Button("Main Menu", self._menu), 1)
        layout2.add_widget(Button("Reset", self._reset), 2)

        self.fix()

    def _next(self) -> None:
        # Call game scene with level +1 ?
        raise NextScene('game')

    def _menu(self) -> None:
        raise NextScene('mainMenu')

    def _reset(self) -> None:
        raise NextScene('game')


class EndScreenScene(Scene):
    """End screen scene"""

    def __init__(self, screen: Screen):
        width = 70
        height = 20

        level = 1
        time = 12.3

        state = True

        x_start = (screen.width - width)//2
        y_start = (screen.height - height)//2

        text = "Level Failed"
        if state:
            text = "Level Complete!"

        s1_width = max(map(len, str(FigletText(text, font='small')).split("\n")))
        s2_width = max(map(len, str(FigletText(str(level), font='small')).split("\n")))

        effects = [Print(
            screen,
            Box(width, height),
            x=x_start,
            y=y_start,
            colour=TEXT_COLOUR
        ), Print(
            screen,
            FigletText(text, font="small"),
            x=(width - s1_width)//2 + x_start,
            y=y_start + 8
        ), Print(
            screen,
            FigletText(str(level), font="small"),
            x=(width - s2_width)//2 + x_start,
            y=y_start + 2,
            colour=TEXT_COLOUR
        )
        ]

        effects.append(EndScreen(state, screen, time, x_start, width, y_start, height))
        duration = -1
        clear = True
        name = "endScreen"
        super(EndScreenScene, self).__init__(
            effects,
            duration,
            clear,
            name
        )


if __name__ == "__main__":
    Screen.wrapper(EndScreenScene, catch_interrupt=True)
