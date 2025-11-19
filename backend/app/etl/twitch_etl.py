import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from common import log_info, log_error

load_dotenv()
DB_URL = os.getenv("DB_URL")
TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_OAUTH = os.getenv("TWITCH_OAUTH")
TWITCH_USER_ID = os.getenv("TWITCH_USER_ID")

def fetch_twitch_followers():
    url = f"https://api.twitch.tv/helix/users/follows?to_id={TWITCH_USER_ID}"
    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {TWITCH_OAUTH}"
    }
    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        data = resp.json().get("data", [])
        df = pd.json_normalize(data)
        df["fetched_at"] = datetime.utcnow()
        log_info(f"Fetched {len(df)} followers from Twitch")
        return df
    except Exception as e:
        log_error(f"Error fetching Twitch followers: {e}")
        return pd.DataFrame()

def store_followers(df: pd.DataFrame):
    engine = create_engine(DB_URL)
    df.to_sql("twitch_followers", engine, if_exists="append", index=False)
    log_info("Followers stored in DB")

if __name__ == "__main__":
    df = fetch_twitch_followers()
    if not df.empty:
        store_followers(df)
