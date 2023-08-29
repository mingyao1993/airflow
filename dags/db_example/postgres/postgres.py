import datetime
from os import path, environ

from airflow.decorators import dag
from airflow.providers.postgres.operators.postgres import PostgresOperator


@dag(
    start_date=datetime.datetime(2023, 1, 1),
    schedule="@daily",
    render_template_as_native_obj=True,
    template_searchpath=path.join(path.dirname(path.abspath(__file__))) + '/sql'
)
def postgres_example():
    environ['AIRFLOW_CONN_POSTGRES_EXAMPLE'] = 'postgresql://user1:password123@postgres-example:5432/postgres'

    create_table1 = PostgresOperator(
        postgres_conn_id='postgres_example',
        task_id="create_table1",
        sql='create_table1.sql'
    )

    populate_table1 = PostgresOperator(
        postgres_conn_id='postgres_example',
        task_id="populate_table1",
        sql='populate_table1.sql'
    )
    get_table1 = PostgresOperator(
        postgres_conn_id='postgres_example',
        task_id="get_table1",
        sql='get_table1.sql'
    )

    create_table1 >> populate_table1 >> get_table1


postgres_example()
