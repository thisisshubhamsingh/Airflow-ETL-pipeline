from extract import extract_multi_files
from config_loader import Base_path
from transform import transform
from load import load
from sqlalchemy import create_engine
import pandas as pd


#df_check = pd.read_sql("SELECT * FROM final_table LIMIT 5" , engine)
#print(df_check)


from sqlalchemy import inspect

engine = create_engine("sqlite:///etl.db")

inspector = inspect(engine)
print("Table: ", inspector.get_table_names())
    