from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'student',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='cat_pipeline',
    default_args=default_args,
    description='Pipeline crawl → clean → save mèo 🐱',
    schedule_interval='0 9 * * *',  # 9h sáng mỗi ngày
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    crawl_cat = BashOperator(
        task_id='crawl_cat',
        bash_command='python /opt/airflow/dags/app/crawl.py'
    )

    transform_cat = BashOperator(
        task_id='transform_cat',
        bash_command='python /opt/airflow/dags/app/transform.py'
    )

    save_cat = BashOperator(
        task_id='save_cat',
        bash_command='python /opt/airflow/dags/scripts/save.py'
    )

    crawl_cat >> transform_cat >> save_cat
