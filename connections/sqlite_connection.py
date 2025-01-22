import logging

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from typing_extensions import Self

from connections.idatabase_connection import ConnectionConfig, IDatabaseConnection

log = logging.getLogger()


class SQLiteConnection(IDatabaseConnection):
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
        config = ConnectionConfig.from_env()

        if config.dsn is not None:
            return cls(config.dsn)

        raise ValueError("SQLite DSN not found in environment variables")
