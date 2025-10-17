import pendulum
# Airflow 3.0 부터 아래 경로로 import 합니다.
from airflow.sdk import DAG
from airflow.providers.smtp.operators.smtp import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    send_email_task = EmailOperator(
        task_id='send_email_task',
        conn_id='conn_smtp_gmail',      # Airflow 3.0 
        to='kish1919@gmail.com',       
        subject='Airflow Email',
        html_content='Airflow is sent successfully'
    )