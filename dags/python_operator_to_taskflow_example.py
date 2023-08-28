import datetime

from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator


# Pass return value from traditional python operator task to decorator task
@dag(
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily",
    render_template_as_native_obj=True
)
def python_operator_to_taskflow():
    def task_a():
        return {"task_a": "value_a"}

    task_a_operator = PythonOperator(
        task_id='task_a',
        python_callable=task_a
    )

    @task
    def task_b(obj):
        print(f"Task A Value: {obj}")

    task_b(obj=task_a_operator.output)


python_operator_to_taskflow()
