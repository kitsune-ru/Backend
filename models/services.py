from pydantic import BaseModel
from typing import Optional


class Service(BaseModel):
    id: Optional[str]
    service_name: str
    status: bool
    description: str


class ServiceIn(BaseModel):
    service_name: str
    description: str
    status: bool
