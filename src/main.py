import sys

from asciimatics.exceptions import ResizeScreenError
from asciimatics.screen import Screen

from game import GameScene
from main_menu import MainMenuScene
from end_screen import EndScreenScene
from level_screen import LevelSelectScene


def start(screen, scene):
    scenes = []
    scenes.append(MainMenuScene(screen))  # name = "mainMenu"
    scenes.append(GameScene(screen))  # name = "game"
    scenes.append(EndScreenScene(screen)) # name="endScreen"
    scenes.append(LevelSelectScene(screen)) # name="levelSelect"
    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)


if __name__ == "__main__":
    last_scene = None
    while True:
        try:
            print(last_scene)
            Screen.wrapper(start, catch_interrupt=True, arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene
