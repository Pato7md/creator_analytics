from fastapi import APIRouter
from ..etl.twitch_etl import fetch_twitch_followers, store_followers

router = APIRouter(prefix="/twitch", tags=["Twitch"])

@router.get("/followers")
def get_followers():
    df = fetch_twitch_followers()
    if not df.empty:
        store_followers(df)
    return df.to_dict(orient="records")
