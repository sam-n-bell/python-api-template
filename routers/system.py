from fastapi import APIRouter
from models.responses.healthcheck import DBCheck, System
from settings import PG_DB
from database.utils import validate_db_connection, get_postgres_conn_str, get_db_session

router = APIRouter(
    prefix="/system",
    tags=["system"]
)


@router.get("/dbcheck", response_model=DBCheck, response_model_exclude_unset=True)
def check_postgres_connection():
    return validate_db_connection(
        db_session=get_db_session(get_postgres_conn_str()),
        database_name=PG_DB
    )


@router.get("/", response_model=System, response_model_exclude_unset=True)
def check_api_up():
    return System(
        available=True
    )