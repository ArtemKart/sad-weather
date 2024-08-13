from dotenv import load_dotenv
import os
from dataclasses import dataclass
from typing import Iterator, Self

from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session


from sqlalchemy import create_engine

load_dotenv()

@dataclass(frozen=True)
class PostgresConfig:
    dbname: str
    user: str
    password: str
    port: str
    host: str

    @property
    def connection_string(self) -> str:
        return f'postgresql://{self.user}:{self.password}@' \
               f'{self.host}:{self.port}/{self.dbname}'

    @classmethod
    def from_env(cls) -> Self:
        return PostgresConfig(
            dbname=os.getenv("PGNAME"),
            user=os.getenv("PGUSER"),
            password=os.getenv("PGPASSWORD"),
            port=os.getenv("PGPORT"),
            host=os.getenv("PGHOST"),
        )

postgres_config = PostgresConfig.from_env()
_engine = create_engine(postgres_config.connection_string)
_session_maker = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


def set_engine(db_engine: Engine):
    global _engine, _session_maker
    _engine = db_engine
    _session_maker = sessionmaker(
        autocommit=False, autoflush=False, bind=_engine)


def get_session() -> Iterator[Session]:
    global _session_maker
    session = _session_maker()

    try:
        yield session
    finally:
        session.close()


def get_engine() -> Engine:
    return _engine
