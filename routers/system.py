from fastapi import APIRouter
from models.responses.healthcheck import DBCheck, System
from database import pg
from settings import PG_DB, APP_NAME

router = APIRouter(
    prefix="/system",
    tags=["system"]
)


@router.get("/dbcheck", response_model=DBCheck, response_model_exclude_unset=True)
def check_db_connection():
    successful = pg.validate_pg_connection()
    return DBCheck(
        available=successful,
        details="unable to connect; check connection string" if not successful else None,
        name=PG_DB
    )


@router.get("/", response_model=System, response_model_exclude_unset=True)
def check_api_up():
    return System(
        name=APP_NAME,
        available=True
    )