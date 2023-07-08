from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

from models.responses.healthcheck import Check
from database import validate_db_connection, get_postgres_conn_str, get_db_session

router = APIRouter(
    prefix="/system",
    tags=["system"]
)


@router.get("/db", response_model=Check, response_model_exclude_unset=True)
def check_postgres_connection(db: Session = Depends(get_db_session)):
    return Check(
        available=validate_db_connection(db_session=db)
    )


@router.get("/", response_model=Check, response_model_exclude_unset=True)
def check_api_up():
    return Check(
        status="I'm up!"
    )