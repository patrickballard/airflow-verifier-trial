from datetime import datetime

from airflow.sdk import DAG, CronDataIntervalTimetable
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="daily_report",
    start_date=datetime(2024, 1, 1),
    schedule=CronDataIntervalTimetable("@daily", timezone="UTC"),
    catchup=False,
) as dag:
    BashOperator(
        task_id="build_report",
        bash_command="echo building the report for {{ ds }}",
    )
