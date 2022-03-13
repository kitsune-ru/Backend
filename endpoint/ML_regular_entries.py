from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.ML_regular_entries import ML_regular_entries
from repository.ML_regular_entries import ML_regular_entries as rep_ML_regular_entries

router = APIRouter()


@router.get("/", response_model=List[ML_regular_entries])
async def get_all_cluster_regular_entries():
    return await rep_ML_regular_entries.get_all()
