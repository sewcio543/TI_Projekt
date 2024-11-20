import re
from environs import Env
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import logging

log = logging.getLogger()

def get_db_url_from_env(user=None, password=None, host=None, port=None, database=None):

    env = Env()
    env.read_env()  # Read .env into os.environ

    if env.str('PG_DSN', None):
        return env.str('PG_DSN')

    pg_user = env.str('PG_USER', default='postgres')
    pg_password = env.str('PG_PASSWORD', default='postgres')
    pg_host = env.str('PG_HOST', default='localhost')
    pg_port = env.int('PG_PORT', default=5432)
    pg_database = env.str('PG_DB', default='postgres')

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

    return f"postgresql+asyncpg://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}"


def init_postgres_ctx(dsn='dsn', pool_max=5, pool_overflow=10, ):
    """Async initialization function for postgres connection

    :param app: aiohttp app.
    :param name:
    :param dsn_key:
    :param session_key:
    :return: engine
    """

    dsn_log = obfuscate_password(dsn)
    engine = create_async_engine(
        dsn,
        pool_pre_ping=True,
        pool_timeout=2 * 60,
        pool_size=pool_max,
        max_overflow=pool_overflow,
        # json_serializer=dumps,
        # json_deserializer=loads
    )
    async_session = async_sessionmaker(engine, expire_on_commit=False)


    log.info(
        f'Created postgres pool (max: {pool_max}/overflow: {pool_overflow}) and connected to {dsn_log}. '
    )

    return async_session




def obfuscate_password(dsn):
    """Helper function to replace the password of a dsn with asterisks

    :param dsn: String of the dsn to obfuscate.
    :return: The obfuscated dsn string.
    """

    reg = (
        r'^(?P<conn>.*?):\/\/'
        r'(?P<user>.*?):(?P<passwd>.*)@'
        r'(?P<addr>[^\(]*):(?P<port>[^\)]*)\/'
        r'(?P<dbname>.*?)$'
    )
    return re.sub(reg, r'\g<conn>://\g<user>:*****@\g<addr>:\g<port>/\g<dbname>', dsn)