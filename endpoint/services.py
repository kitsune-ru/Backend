from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.services import Service, ServiceIn
from endpoint.depends import get_service_repository, get_report_repository, get_current_user, get_user_repository
from models.user import User
from repository.users import UserRepository
from repository.services import ServiceRepository
from repository.reports import ReportRepository
from models.reports import Reports
from models.ML_cluster_center import ML_cluster_center
from repository.ML_cluster_center import ML_cluster_center as rep_ML_center
from endpoint.depends import get_service_repository, get_ML_emotion_repository, get_ML_regular_entries_repository, get_ML_cluster_center_repository
from models.ML_emotion import ML_emotion
from repository.ML_emotion import ML_emotionRepository as rep_ML_emotion
from models.ML_regular_entries import ML_regular_entries
from repository.ML_regular_entries import ML_regular_entries as rep_ML_regular_entries

router = APIRouter()


# @router.get("/{service_name}", response_model=Service)
# async def get_service(service_name: str,
#                      services: ServiceRepository = Depends(get_service_repository)):
#    return await services.get_by_service_name(service_name)

@router.get("/", response_model=List[Service])
async def get_service(services: ServiceRepository = Depends(get_service_repository)):
    return await services.get_all()


@router.get("/{id}/reports", response_model=List[Reports])
async def get_reports_for_service(id: str,
                                  reports: ReportRepository = Depends(get_report_repository),
                                  limit: int = 100,
                                  skip: int = 0):
    return await reports.get_by_reports_name(id, limit=limit, skip=skip)


@router.get("/{id}/ML_cluster_center", response_model=List[ML_cluster_center])
async def get_all_cluster_center(ML_cluster_cent: rep_ML_center = Depends(get_ML_cluster_center_repository)):
    return await ML_cluster_cent.get_all()


@router.get("/{id}/ML_emotion", response_model=List[ML_emotion])
async def get_all_cluster_emotion(ML_emotion: rep_ML_emotion = Depends(get_ML_emotion_repository)):
    return await ML_emotion.get_all()


@router.get("/{id}/ML_regular_entries", response_model=List[ML_regular_entries])
async def get_all_cluster_regular_entries(ML_reg_ent: rep_ML_regular_entries = Depends(get_ML_regular_entries_repository)):
    return await ML_reg_ent.get_all()


@router.post("/", response_model=Service)
async def create_service(
        service: ServiceIn,
        services: ServiceRepository = Depends(get_service_repository),
        users: UserRepository = Depends(get_user_repository),
        current_user: User = Depends(get_current_user)):
    user = await users.get_by_id(id=current_user.id)
    if user is None or current_user.role != "admin":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="you are not eliegeble to do this")
    return await services.create(s=service)


@router.put("/{id}", response_model=Service)
async def update_service(
        id: int,
        service: ServiceIn,
        services: ServiceRepository = Depends(get_service_repository),
        users: UserRepository = Depends(get_user_repository),
        current_user: User = Depends(get_current_user)):
    user = await users.get_by_id(id=current_user.id)
    if user is None or current_user.role != "admin":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="you are not eliegeble to do this")
    return await services.update(id=id, s=service)


@router.delete("/{id}")
async def delete_job(id: int,
                     services: ServiceRepository = Depends(get_service_repository),
                     current_user: User = Depends(get_current_user),
                     users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_id(id=current_user.id)
    if user is None or current_user.role != "admin":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="you are not eliegeble to do this")
    result = await services.delete_service(id=id)
    return {"status": True}
