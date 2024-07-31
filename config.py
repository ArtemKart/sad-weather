import os

from pydantic_settings import BaseSettings, SettingsConfigDict


DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Config(BaseSettings):
    api_key: str
    model_config = SettingsConfigDict(env_file=DOTENV)


config = Config()
