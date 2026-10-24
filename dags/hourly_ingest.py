from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def ingest(**context):
    hour = context["execution_date"].strftime("%Y-%m-%dT%H")
    print(f"ingesting events for hour {hour}")


with DAG(
    dag_id="hourly_ingest",
    start_date=datetime(2024, 1, 1),
    schedule="@hourly",
    catchup=False,
) as dag:
    PythonOperator(task_id="ingest_events", python_callable=ingest)
