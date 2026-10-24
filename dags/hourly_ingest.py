from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def ingest(**context):
    hour = context["execution_date"].strftime("%Y-%m-%dT%H")
    print(f"ingesting events for hour {hour}")


with DAG(
    dag_id="hourly_ingest",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",
    catchup=False,
) as dag:
    PythonOperator(task_id="ingest_events", python_callable=ingest)
