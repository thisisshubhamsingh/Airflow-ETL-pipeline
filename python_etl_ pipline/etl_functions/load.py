from sqlalchemy import create_engine
from config_loader import Base_path
import pandas as pd
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

log = logging.getLogger(__name__)


def load():

    df = pd.read_csv(f"{Base_path}/final_data.csv")

    engine = create_engine("sqlite:///etl.db")

    with engine.begin() as conn:
        df.to_sql("final_table", conn, if_exists="replace", index=False)

    log.info(f"Loaded: {len(df)} rows into final table")

    print(df.shape)
    print(df.head())

    

load()









