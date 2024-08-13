from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, default=datetime.utcnow)
    timezone = Column(String(255))
    max_temp = Column(Float)
    min_temp = Column(Float)
    pressure = Column(Float)
    conditions = Column(String(255))

    def __repr__(self):
        return (
            f"Today is {self.date}. It is a beautiful day.. or not. "
            f"Today's temperature range is from {self.min_temp} to {self.max_temp}."
        )
