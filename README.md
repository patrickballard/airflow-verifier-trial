# airflow-verifier-trial

A small Airflow 2 project, used as a demo for [Airflow Migration Verifier](https://github.com/patrickballard/airflow-migration-verifier).

- `dags/daily_report.py`: `@daily`, a `BashOperator` that uses `{{ ds }}`
- `dags/cleanup_tmp.py`: `start_date=days_ago(2)`
- `dags/hourly_ingest.py`: `@hourly`, a `PythonOperator` that reads `context["execution_date"]`

## Demo: failing vs passing

Both PRs are checked by [`.github/workflows/verify-airflow-3.yml`](.github/workflows/verify-airflow-3.yml), the verify workflow from the action's Quickstart.

- ❌ [PR #1](https://github.com/patrickballard/airflow-verifier-trial/pull/1), migrated with `ruff check --select AIR --fix` and a pin bump, **fails** ([run](https://github.com/patrickballard/airflow-verifier-trial/actions/runs/40110340024)):
  - `daily_report`: `{{ ds }}` renders a day later on 25 of 25 runs (Airflow 2: `2024-01-15`, Airflow 3: `2024-01-16`, for the run firing 2024-01-16 00:00 UTC);
  - `cleanup_tmp`: doesn't import on Airflow 3, because `days_ago` was removed;
  - `hourly_ingest`: still reads `context["execution_date"]`, which Airflow 3 removed.
- ✅ [PR #5](https://github.com/patrickballard/airflow-verifier-trial/pull/5), opened by the action's migrate mode ([`.github/workflows/airflow-3.yml`](.github/workflows/airflow-3.yml), [run](https://github.com/patrickballard/airflow-verifier-trial/actions/runs/40110571348)), **passes** ([run](https://github.com/patrickballard/airflow-verifier-trial/actions/runs/40110745663)). It pins the timetables, rewrites `days_ago` and `execution_date`, and raises the pin to 3.3.2.

Closed PRs #2–#4 are from earlier test rounds.
