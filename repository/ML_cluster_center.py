from typing import List, Mapping

from models.ML_cluster_center import ML_cluster_center
from repository.base import BaseRepository
from db.ML_cluster_center import ML_cluster_center as ml_cl_c


class ML_cluster_centerRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[ML_cluster_center]:
        query = ml_cl_c.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)
