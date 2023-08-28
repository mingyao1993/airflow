from airflow.models import DagBag


def test_dag_loaded():
    dag_bag = DagBag(include_examples=False)

    print(dag_bag.dag_ids)

    assert dag_bag.dag_ids != []
    assert dag_bag.import_errors == {}

