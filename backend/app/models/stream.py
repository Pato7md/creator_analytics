from fbprophet import Prophet
import pandas as pd
import os
import joblib

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")
os.makedirs(MODEL_DIR, exist_ok=True)

def build_forecast(df: pd.DataFrame, date_col="date", target_col="follower_count", model_name="forecast_model.pkl"):
    df = df.rename(columns={date_col: "ds", target_col: "y"})
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)
    joblib.dump(model, os.path.join(MODEL_DIR, model_name))
    return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
