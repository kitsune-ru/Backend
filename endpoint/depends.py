from fastapi import Depends, HTTPException, status

from repository.users import UserRepository
from repository.services import ServiceRepository
from repository.reports import ReportRepository
from repository.ML_cluster_center import ML_cluster_centerRepository
from repository.ML_emotion import ML_emotionRepository
from repository.ML_regular_entries import ML_regular_entriesRepository
from db.base import database
from core.security import JWTBearer, decode_access_token
from models.user import User


def get_ML_cluster_center_repository() -> ML_cluster_centerRepository:
    return ML_cluster_centerRepository(database)


def get_ML_emotion_repository() -> ML_emotionRepository:
    return ML_emotionRepository(database)


def get_ML_regular_entries_repository() -> ML_regular_entriesRepository:
    return ML_regular_entriesRepository(database)


def get_user_repository() -> UserRepository:
    return UserRepository(database)


def get_service_repository() -> ServiceRepository:
    return ServiceRepository(database)


def get_report_repository() -> ReportRepository:
    return ReportRepository(database)


async def get_current_user(
        users: UserRepository = Depends(get_user_repository),
        token: str = Depends(JWTBearer()),
) -> User:
    cred_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credentials are not valid")
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exception
    email: str = payload.get("sub")
    if email is None:
        raise cred_exception
    user = await users.get_by_email(email=email)
    if user is None:
        return cred_exception
    return user
