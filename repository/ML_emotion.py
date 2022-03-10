from typing import List, Mapping

from models.ML_emotion import ML_emotion
from repository.base import BaseRepository
from db.ML_emotion import ML_emotion as ml_em


class ML_emotionRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[ML_emotion]:
        query = ml_em.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)
