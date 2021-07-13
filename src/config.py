import os
from pathlib import Path

from pydantic import BaseSettings

root_dir = Path(os.path.dirname(__file__)).parent


class GeneralSettings(BaseSettings):
    GAME_LOGO_PATH = (root_dir / "docs/images/game-avatar.png").absolute()


general_settings = GeneralSettings()
