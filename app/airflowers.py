from airflow import DAG
from airflow.operators import PythonOperator
from datetime import datetime
import transform_data
import extract_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime.now(),
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_success': False,
    'retries': 1
}

dag = DAG('project_dag', default_args=default_args, schedule_interval='@daily')

python_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract_data.main,
    dag=dag
)

python_task2 = PythonOperator(
    task_id='transform_task',
    python_callable=transform_data.main,
    dag=dag
)

python_task >> python_task2