import sys

from asciimatics.exceptions import ResizeScreenError
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from end_screen import EndScreenScene
from game import GameScene
from level_screen import LevelSelectScene
from main_menu import MainMenuScene


def start(screen: Screen, scene: Scene) -> None:
    """Starts game scenes"""
    scenes = []
    scenes.append(MainMenuScene(screen))  # name = "mainMenu"
    scenes.append(GameScene(screen))  # name = "game"
    scenes.append(EndScreenScene(screen))  # name="endScreen"
    scenes.append(LevelSelectScene(screen))  # name="levelSelect"
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
