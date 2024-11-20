import re
from environs import Env

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