from datetime import datetime
from airflow.sdk import dag
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator

@dag(schedule=None, start_date=datetime(2026, 1, 1), catchup=False, tags=["databricks"])
def run_databricks_job():

    DatabricksRunNowOperator(
        task_id="run_airflow_test_job",
        databricks_conn_id="databricks_default",
        job_id=422279207196940,  # replace with your Job ID
        notebook_params={"name": "Jayanth"},
    )

run_databricks_job()