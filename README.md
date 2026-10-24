# airflow-verifier-trial

A small Airflow 2 project, used as a trial repo for [Airflow Migration Verifier](https://github.com/patrickballard/airflow-migration-verifier).

- `dags/daily_report.py`: `@daily`, a `BashOperator` that uses `{{ ds }}`
- `dags/cleanup_tmp.py`: `start_date=days_ago(2)`
- `dags/hourly_ingest.py`: `@hourly`, a `PythonOperator` that reads `context["execution_date"]`
