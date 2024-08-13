from datetime import datetime
from typing import Any, Self

from dataclasses import dataclass


@dataclass
class WeatherData:
    date: datetime
    timezone: str
    max_temp: float
    min_temp: float
    pressure: float
    conditions: str

    @classmethod
    def from_dict(cls, data: dict[Any, Any]) -> list[Self]:

        return [WeatherData(
                date=datetime.strptime(day["datetime"], "%Y-%m-%d"),
                timezone=data["timezone"],
                max_temp=day["tempmax"],
                min_temp=day["tempmin"],
                pressure=day["pressure"],
                conditions=day["conditions"]
            ) for day in data["days"] ]
