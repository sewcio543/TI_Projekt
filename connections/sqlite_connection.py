import logging

from environs import Env
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from typing_extensions import Self

from connections.idatabase_connection import IDatabaseConnection

log = logging.getLogger()


class SQLiteConnection(IDatabaseConnection):
    def connect(self, **kwargs) -> AsyncSession:
        engine = self.get_engine(**kwargs)
        async_session = async_sessionmaker(engine, expire_on_commit=False)
        return async_session()

    def get_engine(self, **kwargs) -> AsyncEngine:
        engine = create_async_engine(
            self._connection_string,
            pool_pre_ping=True,
        )
        dsn_log = self._obfuscate_password()
        log.info(f"Created sqlite engine and connected to {dsn_log}.")
        return engine

    @classmethod
    def from_env(
        cls,
        user=None,
        password=None,
        host=None,
        port=None,
        database=None,
    ) -> Self:
        env = Env()
        env.read_env()

        if env.str("SQLITE_DSN", None):
            return cls(env.str("SQLITE_DSN"))

        raise ValueError("SQLite DSN not found in environment variables")
