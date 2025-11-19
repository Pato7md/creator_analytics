from fastapi import APIRouter
from ..etl.common import log_info
import pandas as pd

router = APIRouter(prefix="/tiktok", tags=["TikTok"])

@router.get("/followers")
def get_tiktok_followers():
    # Dummy Implementation, echte API später
    df = pd.DataFrame({
        "username": ["user1", "user2"],
        "followers": [150, 200],
        "fetched_at": pd.Timestamp.now()
    })
    log_info(f"Fetched {len(df)} TikTok followers (dummy)")
    return df.to_dict(orient="records")
