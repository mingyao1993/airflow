import datetime

from airflow.decorators import dag, task


# Pass return value from one decorator task to another decorator task
@dag(
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily",
    render_template_as_native_obj=True
)
def taskflow_to_taskflow():
    @task
    def task_a():
        return {"task_a": "value_a"}

    @task
    def task_b(obj):
        print(f"Task A Value: {obj}")

    task_b(obj=task_a())


taskflow_to_taskflow()
