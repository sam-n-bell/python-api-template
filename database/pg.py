import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import structlog

logger = structlog.get_logger("APP")

def get_postgres_conn_str():
    DIALECT = settings.PG_DIALECT
    USER = settings.PG_USER
    PASSWORD = settings.PG_PWD
    HOST = settings.PG_HOST
    PORT = settings.PG_PORT
    DB = settings.PG_DB
    conn = f'{DIALECT}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    logger.info(conn)
    return conn



def get_postgres():
    engine = create_engine(get_postgres_conn_str(), pool_pre_ping=True)
    logger.info(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    return Session()


def validate_pg_connection():
    try:
        pg = get_postgres()
        pg.connection()
        return True
    except Exception as e:
        logger.error(f'Unsuccessful PG connection', error=str(e))
        return False

