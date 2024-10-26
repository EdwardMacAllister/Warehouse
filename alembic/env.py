from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# импортируем ваши модели данных
from Bot.database.models import Base  # Предположим, что ваши модели базируются на SQLAlchemy Base

# Конфигурация Alembic
config = context.config

# Если необходимо, подгружаем файл конфигурации логирования.
fileConfig(config.config_file_name)

# Цель для 'autogenerate': указание на объект MetaData с таблицами
target_metadata = Base.metadata


def run_migrations_offline():
    """Запуск миграций в 'offline' режиме."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Запуск миграций в 'online' режиме."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
