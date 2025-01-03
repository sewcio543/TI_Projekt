from __future__ import annotations

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from environs import Env
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker
from typing_extensions import Self


class IDatabaseConnection(ABC):
    def __init__(self, connection: str) -> None:
        self._connection_string = connection

    def connect(self, **kwargs) -> AsyncSession:
        engine = self.get_engine(**kwargs)
        async_session = async_sessionmaker(engine, expire_on_commit=False)
        return async_session()

    @classmethod
    @abstractmethod
    def from_env(cls) -> Self:
        raise NotImplementedError

    @abstractmethod
    def get_engine(self, **kwargs) -> AsyncEngine:
        raise NotImplementedError

    def _obfuscate_password(self) -> str:
        """Helper function to replace the password of a dsn with asterisks

        :param dsn: String of the dsn to obfuscate.
        :return: The obfuscated dsn string.
        """
        reg = (
            r"^(?P<conn>.*?):\/\/"
            r"(?P<user>.*?):(?P<passwd>.*)@"
            r"(?P<addr>[^\(]*):(?P<port>[^\)]*)\/"
            r"(?P<dbname>.*?)$"
        )
        return re.sub(
            reg,
            r"\g<conn>://\g<user>:*****@\g<addr>:\g<port>/\g<dbname>",
            self._connection_string,
        )

    @property
    def url(self) -> str:
        return self._obfuscate_password()


DEFAULT_USER = "user"
DEFAULT_PASSWORD = "MyStrongPassword169."
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 5432
DEFAULT_DATABASE = "db"
DEFAULT_DSN = None


@dataclass
class ConnectionConfig:
    user: str
    password: str
    host: str
    port: int
    database: str
    dsn: Optional[str] = None

    @classmethod
    def from_env(cls) -> ConnectionConfig:
        env = Env()
        env.read_env()

        return ConnectionConfig(
            user=env.str("DB_USER", default=DEFAULT_USER),
            password=env.str("DB_PASSWORD", default=DEFAULT_PASSWORD),
            host=env.str("DB_HOST", default=DEFAULT_HOST),
            port=env.int("DB_PORT", default=DEFAULT_PORT),
            database=env.str("DB_DATABASE", default=DEFAULT_DATABASE),
            dsn=env.str("DB_DSN", default=DEFAULT_DSN),
        )
