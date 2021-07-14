import os
from pathlib import Path

from pydantic import BaseSettings

root_dir = Path(os.path.dirname(__file__)).parent


class GeneralSettings(BaseSettings):
    GAME_LOGO_PATH = (root_dir / "docs/images/game-avatar.png").absolute()

    def new_maze_path(self):
        nr_files = len(os.listdir(f"{root_dir}/docs/mazes"))
        return (root_dir / f"docs/mazes/maze_{nr_files}.pickle").absolute()


general_settings = GeneralSettings()
