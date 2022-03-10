from pydantic import BaseModel
from typing import Optional


class ML_emotion(BaseModel):
    id: Optional[str]
    name: str
    embedding: str
