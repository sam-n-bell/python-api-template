import settings
from database.config import DatabaseConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import structlog

logger = structlog.get_logger("APP")


def get_postgres_conn_str():
    return DatabaseConfig(
        settings.PG_DIALECT,
        settings.PG_USER,
        settings.PG_PWD,
        settings.PG_HOST,
        settings.PG_PORT,
        settings.PG_DB
    ).connection_str


def get_pg_session():
    engine = create_engine(get_postgres_conn_str(), pool_pre_ping=True)
    logger.info(engine)
    session = sessionmaker()
    session.configure(bind=engine)
    return session()


def validate_pg_connection():
    try:
        pg = get_pg_session()
        pg.connection()
        return True
    except Exception as e:
        logger.error(f'Unsuccessful PG connection', error=str(e))
        return False

