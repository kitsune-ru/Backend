from pydantic import BaseModel
from typing import Optional


class Reports(BaseModel):
    id: Optional[str]
    service_id: int
    status: bool
    time: str
