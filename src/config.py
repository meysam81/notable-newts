import os
from pathlib import Path, WindowsPath

from pydantic import BaseSettings

root_dir = Path(os.path.dirname(__file__)).parent


class GeneralSettings(BaseSettings):
    GAME_LOGO_PATH = (root_dir / "docs/images/game-avatar.png").absolute()

    def new_maze_path(self) -> WindowsPath:
        nr_files = len(os.listdir(f"{root_dir}/docs/mazes"))
        return (root_dir / f"docs/mazes/{nr_files}.pickle").absolute()

    def load_maze(self, nr):
        return (root_dir / f"docs/mazes/{nr}.pickle").absolute()


general_settings = GeneralSettings()
