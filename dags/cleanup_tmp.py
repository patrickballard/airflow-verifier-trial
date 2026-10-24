from airflow.utils.dates import days_ago
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

default_args = {"owner": "data-eng", "retries": 1}

with DAG(
    dag_id="cleanup_tmp",
    default_args=default_args,
    start_date=days_ago(2),
    schedule="0 3 * * *",
    catchup=False,
) as dag:
    BashOperator(
        task_id="delete_old_files",
        bash_command="find /tmp/exports -mtime +7 -delete || true",
    )
