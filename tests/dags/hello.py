#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
from airflow.models import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
}

dag = DAG(
    dag_id='hello',
    default_args=default_args,
    description='The first DAG',
    catchup=False,
    schedule_interval=None,
    start_date=datetime.datetime(2021, 1, 1),
    tags=['example'],
)

t1 = BashOperator(
    task_id='print_hello',
    bash_command='echo "Hello dags!"',
    dag=dag
)

t2 = BashOperator(
    task_id='print_hello_again',
    bash_command='echo "Hello dags again!"',
    dag=dag
)

t1 >> t2