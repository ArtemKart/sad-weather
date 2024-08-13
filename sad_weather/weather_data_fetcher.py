import os
from datetime import datetime

import requests
import urllib.parse

from config_parser import ConfigParams
from sad_weather.weather_data import WeatherData


class WeatherDataFetcher:
    def  __init__(self):
        self.api = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timelinemulti"
        self._api_key = self._read_api_key()

    @staticmethod
    def _read_api_key() -> str:
        from dotenv import load_dotenv
        load_dotenv()
        return os.getenv("api_key")

    def fetch_data(self, locations: str, config_params: ConfigParams) -> list[WeatherData]:
        sorted_days = sorted(config_params.dates)
        return self._fetch_data(locations, sorted_days)

    def _fetch_data(self, locations: str, days: list[datetime]) -> [WeatherData]:
        params = {
            "key": self._api_key,
            "locations": urllib.parse.quote(locations),
            "datestart": [str(days[0].date())],
            "dateend": [str(days[len(days)-1].date())],
        }
        req = requests.get(self.api, params)
        data = req.json()
        return WeatherData.from_dict(data)
