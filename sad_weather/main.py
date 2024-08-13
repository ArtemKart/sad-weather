from dataclasses import asdict

from sqlalchemy import insert
from config_parser import ConfigLoader
from sad_weather.db.models import Weather
from sad_weather.utils import get_config_file_path
from sad_weather.weather_data_fetcher import WeatherDataFetcher
from sad_weather.db import get_session


import logging

logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Start process...")
    config_ini_path = get_config_file_path()
    config_params = ConfigLoader(config_ini_path).load()

    fetcher = WeatherDataFetcher()
    data = fetcher.fetch_data(config_params.locations,config_params)
    session = get_session().__next__()
    logger.info("Saving data to database...")
    try:
        for weather_data in data:
            stmt = insert(Weather).values(asdict(weather_data))
            session.execute(stmt)
        session.commit()
        logging.info("Data committed to the database")
    except Exception as e:
        session.rollback()
        logging.error(f"Error occurred while committing data: {e}")
