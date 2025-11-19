from fastapi import FastAPI
from etl.twitch_etl import fetch_twitch_followers, store_followers
from ml.trend_model import build_forecast
import pandas as pd

app = FastAPI(title="Creator Analytics MVP")

@app.get("/api/twitch/followers")
def get_followers():
    df = fetch_twitch_followers()
    if not df.empty:
        store_followers(df)
    return df.to_dict(orient="records")

@app.get("/api/twitch/forecast")
def get_forecast():
    df = pd.read_csv("../../data/dummy/twitch_followers.csv")
    forecast = build_forecast(df)
    return forecast.to_dict(orient="records")
