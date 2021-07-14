from asciimatics.effects import Print
from asciimatics.exceptions import StopApplication
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
        )

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
        layout2.add_widget(Button("Level Select", self._select), 1)
        layout2.add_widget(Button("Reset", self._reset), 2)

        self.fix()

    def _next(self) -> None:
        # To be added
        ...

    def _select(self) -> None:
        # To be added
        ...

    def _reset(self) -> None:
        # To be changed
        raise StopApplication("reset")


def effect(screen: Screen, level: int, state: bool, width: int, height: int) -> tuple[list, int, int]:
    """Gets the effects to show"""
    x_start = (screen.width - width)//2
    y_start = (screen.height - height)//2

    text = "Level Failed"
    if state:
        text = "Level Complete!"

    s1_width = max(map(len, str(FigletText(text, font='small')).split("\n")))
    s2_width = max(map(len, str(FigletText(str(level), font='small')).split("\n")))

    number = [Print(
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

    return number, x_start, y_start


def run(screen: Screen, level: int, state: bool, time: float, width: int, height: int) -> None:
    """Runs the end screen"""
    effects, x_pad, y_pad = effect(screen, level, state, width, height)
    effects.append(EndScreen(state, screen, time, x_pad, width, y_pad, height))
    scenes = [Scene(effects=effects, duration=-1, name="End")]
    screen.play(scenes, stop_on_resize=True, allow_int=True)


def main(screen: Screen) -> None:
    """Main"""
    run(screen, 1, True, 2.4, 70, 20)


Screen.wrapper(main)
