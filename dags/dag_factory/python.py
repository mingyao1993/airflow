def custom_python_operator(task_id, dag, **kwargs):
    
    from airflow.providers.standard.operators.python import PythonOperator
    from pydoc import locate
    
    return PythonOperator(
        dag=dag,
        task_id=task_id,
        python_callable=locate(kwargs['python_callable']),
    )
