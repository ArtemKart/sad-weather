from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
import logging

from sad_weather.main import main

logger = logging.getLogger(__name__)

default_args = {
    "owner": "airflow",
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="process_runner",
    default_args=default_args,
    start_date=datetime(2024, 8, 13, 23),
    schedule="@hourly",
) as dag:
    task = PythonOperator(
        task_id="main",
        python_callable=main,
    )
