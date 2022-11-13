import settings
from dataclasses import dataclass
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import structlog

from models.responses.healthcheck import DBCheck

logger = structlog.get_logger("APP")


@dataclass
class DatabaseConfig:
    dialect: str
    user: str
    password: str
    host: str
    port: str
    db: str

    @property
    def connection_str(self):
        return (
            f'{self.dialect}://'
            f'{self.user}:'
            f'{self.password}@'
            f'{self.host}:'
            f'{self.port}/'
            f'{self.db}'
        )


def get_postgres_conn_str():
    return DatabaseConfig(
        settings.PG_DIALECT,
        settings.PG_USER,
        settings.PG_PWD,
        settings.PG_HOST,
        settings.PG_PORT,
        settings.PG_DB
    ).connection_str


def get_db_session(conn_str):
    engine = create_engine(conn_str, pool_pre_ping=True)
    db_session = scoped_session(sessionmaker(bind=engine))
    return db_session


def validate_db_connection(db_session, database_name=None):
    success = False
    try:
        db_session.connection()
        success = True
    except Exception as e:
        logger.error(f'Unsuccessful connection', db_name=database_name, error=str(e))
    finally:
        if db_session:
            db_session.close()
        return DBCheck(
            available=success,
            name=database_name
        )
