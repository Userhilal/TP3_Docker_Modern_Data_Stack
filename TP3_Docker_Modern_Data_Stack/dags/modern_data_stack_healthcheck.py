from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="modern_data_stack_healthcheck",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["tp3", "docker", "modern-data-stack"],
) as dag:
    check_environment = BashOperator(
        task_id="check_environment",
        bash_command="echo 'Airflow est opérationnel dans le TP3 Modern Data Stack' && date",
    )
