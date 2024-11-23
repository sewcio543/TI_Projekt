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


class PostgresConnection(IDatabaseConnection):
    def connect(self, **kwargs) -> AsyncSession:
        engine = self.get_engine(**kwargs)
        async_session = async_sessionmaker(engine, expire_on_commit=False)
        return async_session()

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
            f"Created postgres engine (max: {pool_max}/overflow: {pool_overflow}) "
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
        env.read_env()  # Read .env into os.environ

        if env.str("PG_DSN", None):
            return cls(env.str("PG_DSN"))

        pg_user = env.str("PG_USER", default="postgres")
        pg_password = env.str("PG_PASSWORD", default="postgres")
        pg_host = env.str("PG_HOST", default="localhost")
        pg_port = env.int("PG_PORT", default=5432)
        pg_database = env.str("PG_DB", default="postgres")

        if user is not None:
            pg_user = user
        if password is not None:
            pg_password = password
        if host is not None:
            pg_host = host
        if port is not None:
            pg_port = port
        if database is not None:
            pg_database = database

        dsn = f"postgresql+asyncpg://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}"
        return cls(dsn)
