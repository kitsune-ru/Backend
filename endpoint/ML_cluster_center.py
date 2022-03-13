from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.ML_cluster_center import ML_cluster_center
from repository.ML_cluster_center import ML_cluster_center as rep_ML_cluster_center

router = APIRouter()


@router.get("/", response_model=List[ML_cluster_center])
async def get_all_cluster_center():
    return await rep_ML_cluster_center.get_all()
