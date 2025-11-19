from fastapi import APIRouter
import pandas as pd
from ..etl.youtube_etl import fetch_youtube_watchtime

router = APIRouter(prefix="/youtube", tags=["YouTube"])

@router.get("/watchtime")
def get_watchtime():
    df = fetch_youtube_watchtime()
    return df.to_dict(orient="records")
