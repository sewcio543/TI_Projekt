import asyncio

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

from api.log import log
from connections.setup import get_connection
from domain.models.db_models import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config


# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    # ! IMPORTANT
    # Assuming migrataions are run localy (not inside running container)
    # than we HAVE to use host=localhost and port=5454
    # which points to DB running inside container (docker-compose)
    connection = get_connection()
    url = connection.url
    log.info(f"Using url: {url}")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    # ! IMPORTANT
    # Assuming migrataions are run localy (not inside running container)
    # than we HAVE to use host=localhost and port=5454
    # which points to DB running inside container (docker-compose)
    connection = get_connection()
    log.info(f"Using url: {connection.url}")
    connectable = connection.get_engine()

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
