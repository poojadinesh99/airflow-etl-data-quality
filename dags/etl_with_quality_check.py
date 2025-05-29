from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import random

def extract_data():
    print("📦 Extracting data...")

def transform_data():
    print("🔄 Transforming data...")

def load_data():
    print("💾 Loading data...")

def data_quality_check():
    print("🧪 Running data quality check...")
    if random.choice([True, False]):
        raise ValueError("❌ Data quality check failed!")
    print("✅ Data quality passed!")

default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='etl_with_data_quality_check',
    schedule_interval='@daily',
    default_args=default_args,
    catchup=False,
    tags=["data-pipeline", "quality-check"],
) as dag:

    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_data
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=transform_data
    )

    load = PythonOperator(
        task_id='load',
        python_callable=load_data
    )

    quality_check = PythonOperator(
        task_id='data_quality_check',
        python_callable=data_quality_check
    )

    extract >> transform >> load >> quality_check
