import datetime

from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator


# Pass return value from decorator task to traditional python operator task
@dag(
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily",
    render_template_as_native_obj=True
)
def taskflow_to_python_operator():
    @task
    def task_a():
        return {"task_a": "value_a"}

    def task_b(obj):
        print(f"Task A Value: {obj}")

    PythonOperator(
        task_id='task_b',
        python_callable=task_b,
        op_args=[task_a()]
    )


taskflow_to_python_operator()
