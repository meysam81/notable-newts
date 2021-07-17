import os

from asciimatics.effects import Print
from asciimatics.exceptions import NextScene
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Label, Layout

from config import root_dir

MAZE_LOC = (root_dir / r"docs/mazes").absolute()

TEXT_COLOUR = Screen.COLOUR_WHITE


class LevelScreen(Frame):
    """Framework for end screen"""

    def __init__(self, screen: Screen, y_pad: int):
        """Initiates end screen"""
        self.text_width = 60
        self.x_pos, self.y_pos = (screen.width-self.text_width)//2, y_pad+2
        super(LevelScreen, self).__init__(
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

        levels = len(os.listdir(MAZE_LOC))

        rows = levels//4

        layouts = [Layout([1, 1, 1, 1]) for _ in range(rows)]

        bottom = Layout([2])

        if levels % 4:
            layouts.append(Layout([1]*(levels % 4)))

        for layout in layouts:
            self.add_layout(layout)

        self.add_layout(bottom)

        if levels % 4:
            j = 0
            for j in range(len(layouts) - 1):
                for i in range(4):
                    layouts[j].add_widget(Button(f"Level {j*4+i}", lambda i=j*4+i: self._level(i)), i)

            for i in range(levels % 4):
                layouts[-1].add_widget(Button(f"Level {j*4 + i}", lambda i=j*4+i: self._level(i)), i)

        else:
            for j in range(len(layouts)):
                for i in range(4):
                    layouts[j].add_widget(Button(f"Level {j*4+i}", lambda i=j*4+i: self._level(i)), i)

        bottom.add_widget(Label(""), 0)
        bottom.add_widget(Button("Exit", self._quit), 0)

        self.fix()

    def _level(self, num: int) -> None:
        # To be added
        print(num)
        raise NextScene("game")

    def _quit(self) -> None:
        # To be changed
        raise NextScene("mainMenu")


class LevelSelectScene(Scene):
    """Level scene"""

    def __init__(self, screen: Screen):
        s_width = max(map(len, str(FigletText("Level Select", font='small')).split("\n")))
        s_height = len(str(FigletText("Level Select", font='small')).split("\n"))

        effects = [Print(
            screen,
            FigletText("Level Select", font='small'),
            x=(screen.width - s_width)//2,
            y=1,
            colour=TEXT_COLOUR
        )
        ]

        effects.append(LevelScreen(screen, s_height))

        duration = -1
        clear = True
        name = "levelSelect"
        super(LevelSelectScene, self).__init__(
            effects,
            duration,
            clear,
            name
        )


if __name__ == "__main__":
    Screen.wrapper(LevelSelectScene, catch_interrupt=True)
