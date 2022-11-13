from pydantic import BaseModel


class Check(BaseModel):
    status: str = None
    available: bool = None
    details: str = None
    name: str


class DBCheck(Check):
    pass


class System(Check):
    pass
