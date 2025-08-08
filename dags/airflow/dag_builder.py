import pathlib
import yaml

from datetime import datetime
from airflow import DAG
from pydoc import locate

extension = "yml"

def create_dag(dag_config: dict) -> DAG:
    dag_id = dag_config['dag_id']

    # Check if the DAG ID already exists in globals
    if dag_id in globals():
        raise ValueError(f"DAG ID '{dag_id}' already exists. Please use a unique dag_id.")
    
    # Create the DAG instance
    dag = DAG(
        dag_id=dag_id,
        start_date=datetime.strptime(dag_config['start_date'], '%Y-%m-%d'),
        schedule=dag_config.get('schedule', None),
        description=dag_config.get('description', ''),
        tags=dag_config['tags']
    )
    create_tasks(dag=dag, tasks=dag_config['tasks'])

    return dag


def create_tasks(dag: DAG, tasks: dict) -> None:
    for task_id, task_config in tasks.items():
        operator = locate(task_config['operator'])
        task = operator(
            task_id=task_id,
            dag=dag,
            **task_config.get('arguments', {})
        )

        # Set dependencies if specified
        dependencies = task_config.get('dependencies')
        if dependencies:
            for dependency in dependencies:
                upstream_task = dag.get_task(dependency)
                upstream_task.set_downstream(task)

        


def load_yaml_dags() -> None: 
    for file in pathlib.Path("dags").rglob(f"*.{extension}"):
        with open(file) as stream:
            try:
                config = yaml.safe_load(stream)
                dag = create_dag(dag_config=config)
                globals()[dag.dag_id] = dag
            except yaml.YAMLError as exc:
                print(exc)
    

load_yaml_dags()
