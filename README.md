Airflow ETL Pipeline (Production-Style)
Project Overview

This project demonstrates a production-style ETL (Extract, Transform, Load) pipeline built using Apache Airflow.
It processes multiple CSV datasets, performs data cleaning and transformation, and loads the final dataset into a database.

The pipeline is fully automated and scheduled using an Airflow DAG.

Raw CSV Files → Extract → Transform → Load → SQLite Database

Extract → Reads multiple CSV files from a directory
Transform → Cleans, merges, and engineers features
Load → Stores processed data into a database

.
├── etl_pipeline.py      # Airflow DAG
├── extract.py           # Data extraction logic
├── transform.py         # Data transformation logic
├── load.py              # Data loading logic
├── config_loader.py     # Config handling
├── config.yaml          # Path configuration
├── app.log              # Logging file
├── etl.db               # SQLite database
└── data/                # Input CSV files


Tech Stack
Python
Apache Airflow
Pandas
SQLAlchemy
SQLite
YAML (Config management)
Logging (Production-style monitoring)

DAG Workflow
The Airflow DAG orchestrates 3 tasks:

extract_data → transform_data → load_data

Defined in: etl_pipeline.py

extract_task >> transform_task >> load_task
Extract Phase
Reads all CSV files from a configured directory
Handles multiple files dynamically
Logs success/failure of each file



Transform Phase
Key transformations:

Column standardization (lowercase, trim)
Missing value handling
Duplicate removal
Data merging (customers, orders, marketing)

Feature engineering:
df["roi"] = df["amount"] / df["marketing_spend"]
Saves final dataset to CSV



Load Phase
Reads transformed data
Loads into SQLite database using SQLAlchemy
Replaces table on each run



Configuration
Config is managed via YAML:

paths:
  base_path: /your/data/folder

Loaded using: config_loader.py



Logging & Monitoring
Logs stored in app.log
Tracks:
File loading
Transform steps
Errors & failures
Final load status


Example logs:
Loaded: 14 rows into final table


Scheduling
DAG runs daily
Retry mechanism included
Email alerts on failure
schedule_interval = "@daily"
retries = 2
retry_delay = 5 minutes



How to Run
1. Start Airflow
airflow webserver
airflow scheduler
2. Place DAG file

Move etl_pipeline.py to:  airflow/dags/

3. Trigger DAG
Open: http://localhost:8080
Enable DAG: etl_pipeline_production
Click ▶ Run

Output
Final CSV: final_data.csv
Database: etl.db
Table: final_table


Key Highlights (Resume-Ready)
Built end-to-end ETL pipeline using Apache Airflow
Automated data ingestion from multiple sources
Implemented data cleaning & feature engineering
Integrated SQLAlchemy for database loading
Designed modular and scalable architecture
Added logging & monitoring for production readiness


Future Improvements
Move from SQLite → PostgreSQL
Add Docker support
Implement XCom for task communication
Add data validation layer (Great Expectations)
Integrate dashboard (Power BI / Tableau)


Author

Shubham Singh
