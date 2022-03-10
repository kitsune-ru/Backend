from typing import List, Optional
from repository.base import BaseRepository
from db.users import users
from models.user import User, UserIn
from core.security import hash_password


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[User]:
        query = users.select().where(users.c.id == id)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def get_by_email(self, email: str) -> User:
        query = users.select().where(users.c.email == email)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def create(self, u: UserIn) -> User:
        user = User(
            username=u.username,
            email=u.email,
            hashed_password=hash_password(u.password),
            role="user"
        )
        values = {**user.dict()}
        values.pop("id", None)
        query = users.insert().values(**values)
        user.id = await self.database.execute(query)
        return user
