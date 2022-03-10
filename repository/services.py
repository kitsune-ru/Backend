from typing import List, Optional

from models.services import Service, ServiceIn
from db.services import services
from repository.base import BaseRepository


class ServiceRepository(BaseRepository):
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Service]:
        query = services.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_service_name(self, service_name: str) -> Service:
        query = services.select().where(services.c.service_name == service_name)
        service = await self.database.fetch_one(query)
        if service is None:
            return None
        return Service.parse_obj(service)

    async def get_by_id(self, id: int) -> Optional[Service]:
        query = services.select().where(services.c.id == id)
        service = await self.database.fetch_one(query)
        if service is None:
            return None
        return Service.parse_obj(service)

    async def create(self, s: ServiceIn) -> Service:
        service = Service(
            service_name=s.service_name,
            description=s.description,
            status=s.status,
        )
        values = {**service.dict()}
        values.pop("id", None)
        query = services.insert().values(**values)
        service.id = await self.database.execute(query)
        return service

    async def update(self, id: int, s: ServiceIn) -> Service:
        service = Service(
            id=id,
            service_name=s.service_name,
            status=s.status,
            description=s.description,
        )
        values = {**service.dict()}
        values.pop("id", None)
        query = services.update().where(services.c.id == id).values(**values)
        await self.database.execute(query)
        return service

    async def delete_service(self, id: int) -> Optional[Service]:
        query = services.delete().where(services.c.id == id)
        return await self.database.execute(query=query)
