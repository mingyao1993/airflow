# Airflow 3

## Overview

This repository provides Airflow 3 DAGs and supporting code for orchestrating data workflows. It includes:

- Modular DAG definitions for various products and domains.
- YAML-based DAG configuration and dynamic DAG loading.
- Example usage and references for local development.

The codebase is structured to support scalable, maintainable, and secure data orchestration using Apache Airflow.

## Requirements

- Python (recommended version: 3.11+)
- [uv](https://uv.pypa.io/) (Python package manager)

## Usage

To use this repository for local Airflow development:

1. **Create a virtual environment using `uv`:**
    ```bash
    uv venv
    ```

2. **Start Airflow in standalone mode:**
    ```bash
    AIRFLOW_HOME=$(pwd)/.local uv run airflow standalone
    ```

3. **Access the Airflow web interface:**  
    Open [http://localhost:8080](http://localhost:8080) in your browser.

All configuration files, credentials, and logs are stored in the `.local` directory within your project. Example DAGs are disabled by default.


## References

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)