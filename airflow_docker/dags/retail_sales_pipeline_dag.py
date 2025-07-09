from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from datetime import datetime, timedelta
import sys
import os
from airflow.providers.papermill.operators.papermill import PapermillOperator

sys.path.append('/opt/airflow/scripts')
from ingestion  import ingest 

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# DAG definition
with DAG(
    dag_id='retail_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for retail sales using Airflow',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    ingest = PythonOperator(
        task_id='ingest',
        python_callable= ingest
    )

    transform = PapermillOperator(
        task_id='transform_data',
        input_nb='/opt/airflow/notebooks/transform.ipynb',   
        output_nb='/opt/airflow/notebooks/transform_executed_notebooks_by_date/out_transform_{{ ds }}.ipynb'
    )

    load = PapermillOperator(
        task_id='load_data',
        input_nb='/opt/airflow/notebooks/data_loading.ipynb',
        output_nb='/opt/airflow/notebooks/data_loading_executed_notebooks_by_date/out_load_{{ ds }}.ipynb'
    )

    ingest >> transform >> load

