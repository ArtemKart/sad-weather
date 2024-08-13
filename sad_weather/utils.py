from pathlib import Path
from typing import Final


CONFIG_FILE_PATH: Final = Path(__file__).parent.parent / "config.ini"


def get_config_file_path() -> Path:
    return CONFIG_FILE_PATH
