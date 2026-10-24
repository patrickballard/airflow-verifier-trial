from datetime import datetime

from airflow.sdk import DAG, CronDataIntervalTimetable
from airflow.providers.standard.operators.python import PythonOperator


def ingest(**context):
    hour = context["logical_date"].strftime("%Y-%m-%dT%H")
    print(f"ingesting events for hour {hour}")


with DAG(
    dag_id="hourly_ingest",
    start_date=datetime(2024, 1, 1),
    schedule=CronDataIntervalTimetable("@hourly", timezone="UTC"),
    catchup=False,
) as dag:
    PythonOperator(task_id="ingest_events", python_callable=ingest)
