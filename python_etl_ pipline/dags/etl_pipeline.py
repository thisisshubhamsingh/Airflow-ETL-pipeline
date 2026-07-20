from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from extract import extract
from transform import transform
from load import load
import logging


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s")


log = logging.getLogger(__name__)



dafault_args = {
    "owner" : "data engineer",
    "start_date" : datetime(2026,7,19),
    "retries" : 2,
    "retry_delay" : timedelta(minutes=5),
    "email_on_failure": True,
    "email": ["shubhamsingh26.83@gmail.com"]
}


with DAG(
    dag_id = "etl_pipeline_production",
    default_args = dafault_args,
    schedule_interval = "@daily",
    catchup= False,
    description= "Production ETL pipeline"
) as dag:
    
    extract_task = PythonOperator(
        task_id = "extract_data",
        python_callable = extract
    )

    transform_task = PythonOperator(
        task_id = "transform_data",
        python_callable = transform
    )

    load_task = PythonOperator(
        task_id = "load_data",
        python_callable = load
    )


    #Dependencies
    extract_task >> transform_task >> load_task





