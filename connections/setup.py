from environs import Env

from connections.idatabase_connection import IDatabaseConnection
from connections.postgres_connection import PostgresConnection
from connections.sqlite_connection import SQLiteConnection
from connections.sqlserver_connection import MSSQLConnection

env = Env()
env.read_env()

DATABASES: dict[str, IDatabaseConnection] = {
    "LOCAL": SQLiteConnection("sqlite+aiosqlite:///database.db"),
    "SQLITE_MEMORY": SQLiteConnection("sqlite+aiosqlite:///:memory:"),
    "POSTGRES": PostgresConnection.from_env(),
    "SQLSERVER": MSSQLConnection.from_env(),
}

DEFAULT_CONNECTION = "SQLSERVER"
DEFAULT = env.str("DATABASE", None) or DEFAULT_CONNECTION


def get_connection(name: str = DEFAULT) -> IDatabaseConnection:
    return DATABASES[name]
