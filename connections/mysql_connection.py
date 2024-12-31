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


class MysqlConnection(IDatabaseConnection):
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
            f"Created mysql engine (max: {pool_max}/overflow: {pool_overflow}) "
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

        if env.str("DSN", None):
            return cls(env.str("DSN"))

        m_user = env.str("USER", default="postgres")
        m_password = env.str("PASSWORD", default="postgres")
        m_host = env.str("HOST", default="localhost")
        m_port = env.int("PORT", default=5432)
        m_database = env.str("DB", default="postgres")

        if user is not None:
            m_user = user
        if password is not None:
            m_password = password
        if host is not None:
            m_host = host
        if port is not None:
            m_port = port
        if database is not None:
            m_database = database
            

        dsn = f"mysql+aiomysql://{m_user}:{m_password}@{m_host}:{m_port}/{m_database}"
        return cls(dsn)
