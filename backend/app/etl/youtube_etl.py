import pandas as pd
from ..etl.common import log_info

def fetch_youtube_watchtime():
    # Dummy Implementation für MVP
    df = pd.read_csv("../../data/dummy/youtube_watchtime.csv")
    log_info(f"Fetched {len(df)} YouTube watchtime records (dummy)")
    return df
