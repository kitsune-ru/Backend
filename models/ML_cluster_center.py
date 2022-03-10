from pydantic import BaseModel
from typing import Optional


class ML_cluster_center(BaseModel):
    id: Optional[str]
    tags: str
    density:float
    embedding: str
    distantion: str