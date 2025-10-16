from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",   # 매일 0시 0분에 시작
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,  # 누락되었던 날들이 랜덤하게 진행되기 때문에 보통 False 로 둔다
) as dag:
    # Create
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command='echo whoami',
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command='echo $HOSTNAME',
    )

    bash_t1  >> bash_t2