import datetime

from airflow.decorators import dag
from airflow.operators.python import PythonOperator


# Pass return value from one traditional python operator task to another traditional python operator task
@dag(
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily",
    render_template_as_native_obj=True
)
def python_operator_to_python_operator():
    def task_a():
        return {"task_a": "value_a"}

    task_a_operator = PythonOperator(
        task_id='task_a',
        python_callable=task_a
    )

    def task_b(obj):
        print(f"Task A Value: {obj}")

    task_b_operator = PythonOperator(
        task_id='task_b',
        python_callable=task_b,
        op_args=[task_a_operator.output]
    )

    task_a_operator >> task_b_operator


python_operator_to_python_operator()
