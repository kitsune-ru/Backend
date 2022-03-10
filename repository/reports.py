from typing import List, Mapping

from models.reports import Reports
from repository.base import BaseRepository
from db.reports import reports


class ReportRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Reports]:
        query = reports.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_reports_name(self, service_id: str) -> List[Reports]:
        query = reports.select().where(reports.c.service_id == service_id)
        return await self.database.fetch_all(query=query)
