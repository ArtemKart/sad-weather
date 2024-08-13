import configparser
import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class ConfigLoaderException(Exception):
    pass


class ConfigLoaderExceptionGroup(ExceptionGroup):
    pass


@dataclass(frozen=True)
class ConfigParams:
    """Class to hold configuration parameters."""
    locations: str
    dates: list[datetime.date]


class ConfigLoader:
    def __init__(self, config_ini_path: Path) -> None:
        _validate_config_ini_path(config_ini_path)
        self.config = configparser.ConfigParser()
        self.config.read(config_ini_path)
        pass


    def load(self) -> ConfigParams:
        return ConfigParams(
            locations=self.config.get("locations", "locations"),
            dates=[
                datetime.strptime(date, "%d.%m.%Y")
                for date in self.config.get("dates", "dates").split(",")
            ],
        )


def _validate_config_ini_path(path: Path) -> None:
    exceptions: list[ConfigLoaderException] = []
    if not path.exists():
        exceptions.append(ConfigLoaderException(f"Path: {path} does not exist."))
    else:
        if not path.suffix == ".ini":
            exceptions.append(
                ConfigLoaderException(f"File extension is {path.suffix}, but .ini is expected.")
            )
    if exceptions:
        raise ConfigLoaderExceptionGroup(
            "While validating ini file, following errors occurred: ",
            exceptions
        )
