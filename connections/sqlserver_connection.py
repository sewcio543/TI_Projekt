import logging

from environs import Env
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from typing_extensions import Self

from connections.idatabase_connection import ConnectionConfig, IDatabaseConnection

log = logging.getLogger()

DEFAULT_DRIVER = "ODBC+Driver+17+for+SQL+Server"


class MSSQLConnection(IDatabaseConnection):
    def get_engine(self, **kwargs) -> AsyncEngine:
        pool_max = kwargs.get("pool_max", 5)
        pool_overflow = kwargs.get("pool_overflow", 10)

        engine = create_async_engine(
            self._connection_string,
            pool_pre_ping=True,
            pool_timeout=2 * 60,
            pool_size=pool_max,
            max_overflow=pool_overflow,
        )
        dsn_log = self._obfuscate_password()
        log.info(
            f"Created mssql engine (max: {pool_max}/overflow: {pool_overflow}) "
            f"and connected to {dsn_log}. "
        )
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
        config = ConnectionConfig.from_env()

        if config.dsn is not None:
            return cls(config.dsn)

        user = user or config.user
        password = password or config.password
        host = host or config.host
        port = port or config.port
        database = database or config.database

        driver = env.str("DRIVER", default=DEFAULT_DRIVER)
        dsn = f"mssql+aioodbc://{user}:{password}@{host}:{port}/{database}?TrustServerCertificate=yes&driver={driver}"
        return cls(dsn)
