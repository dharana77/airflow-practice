from airflow import DAG
from airflow.operators.python import (
    PythonOperator,
    PythonVirtualenvOperator
)


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'PythonOperator',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule=timedelta(days=1),
    start_date=datetime(2023, 8, 12),
    catchup=False,
)

def virtual_function():
    from time import sleep
    print("Sleeping for 5 secs..")
    sleep(5)
    print("Woke up")


virtualenv_task = PythonVirtualenvOperator(
    task_id='basic_virtualenv_task',
    python_callable=virtual_function,
    dag=dag,
)