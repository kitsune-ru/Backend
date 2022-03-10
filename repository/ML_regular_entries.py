from typing import List, Mapping

from models.ML_regular_entries import ML_regular_entries
from repository.base import BaseRepository
from db.ML_regular_entries import ML_regular_entries as ml_re


class ML_regular_entriesRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[ML_regular_entries]:
        query = ml_re.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)
