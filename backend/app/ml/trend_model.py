import pandas as pd
from fbprophet import Prophet
import os
import joblib

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")
os.makedirs(MODEL_DIR, exist_ok=True)

def build_forecast(df: pd.DataFrame, model_name="twitch_forecast.pkl"):
    df = df.rename(columns={"date": "ds", "follower_count": "y"})
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)
    model_path = os.path.join(MODEL_DIR, model_name)
    joblib.dump(model, model_path)
    return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
