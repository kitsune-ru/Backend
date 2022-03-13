from typing import List

from fastapi import APIRouter, Depends

from endpoint.depends import get_ML_emotion_repository
from models.ML_emotion import ML_emotion
from repository.ML_emotion import ML_emotionRepository as rep_ML_emotion

router = APIRouter()


@router.get("/", response_model=List[ML_emotion])
async def get_all_cluster_emotion(ML_emotion: rep_ML_emotion = Depends(get_ML_emotion_repository)):
    return await ML_emotion.get_all()