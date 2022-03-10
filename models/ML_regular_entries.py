from pydantic import BaseModel
from typing import Optional


class ML_regular_entries(BaseModel):
    id: Optional[str]
    text: str
    embedding: str
    label: int
