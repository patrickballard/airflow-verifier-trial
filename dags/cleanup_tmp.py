import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import CronDataIntervalTimetable

default_args = {"owner": "data-eng", "retries": 1}

with DAG(
    dag_id="cleanup_tmp",
    default_args=default_args,
    start_date=pendulum.today("UTC").add(days=-2),
    schedule=CronDataIntervalTimetable("0 3 * * *", timezone="UTC"),
    catchup=False,
) as dag:
    BashOperator(
        task_id="delete_old_files",
        bash_command="find /tmp/exports -mtime +7 -delete || true",
    )
