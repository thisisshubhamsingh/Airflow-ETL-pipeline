from extract import extract_multi_files
import pandas as pd
import logging
from config_loader import Base_path

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

log = logging.getLogger(__name__)


def transform():
    dataframes = extract_multi_files(Base_path)
    log.info("files loaded")

    customers = dataframes["customers_clean.csv"]
    marketing = dataframes["marketing_clean.csv"]
    orders = dataframes["orders_clean.csv"]

    #Cleaning
    for file, df in dataframes.items():
        df.columns = df.columns.str.strip().str.lower()
        log.info("Cleaned all columns")

    #missing values
    customers["email"].fillna("unknown@gmail.com", inplace =True)
    customers["city"].fillna("unknown", inplace =True)
    log.info("repalced all missing values")

    orders.drop_duplicates(inplace=True)
    log.info("droped duplicates")

    orders["amount"].fillna(0, inplace=True)
    log.info("missing amount replaced with zero")


    #merge
    df = orders.merge(customers, on = "customer_id", how = "left")
    df = df.merge(marketing, on = "product", how = "left")
    log.info("merged dataframes")

    #Feature engineering
    df["roi"] = df["amount"]/df["marketing_spend"]
    log.info("created new column: roi")

    #save 
    df.to_csv(f"{Base_path}/final_data.csv", index = False)
    log.info("final data has been saved")



