# Airflow ETL Pipeline with Data Quality Checks

This repository contains an Apache Airflow ETL pipeline that performs extract, transform, and load (ETL) tasks with integrated data quality checks. The data quality checks are simulated and the project also integrates with Great Expectations for data validation.

## Prerequisites

- Docker
- Docker Compose

## Setup and Running

To start the Airflow services along with a PostgreSQL database, run the following command in the root directory of the project:

```bash
docker-compose up
```

This will start three services:
- `postgres`: PostgreSQL database for Airflow metadata
- `airflow-webserver`: Airflow webserver accessible at [http://localhost:8088](http://localhost:8088)
- `airflow-scheduler`: Airflow scheduler to run the DAGs

The Airflow webserver will initialize the database and create an admin user with the following credentials:
- Username: `admin`
- Password: `admin`

## DAG Description

The DAG `etl_with_data_quality_check` runs daily and consists of the following tasks:

1. **extract**: Simulates data extraction.
2. **transform**: Simulates data transformation.
3. **load**: Simulates loading data.
4. **data_quality_check**: Runs a data quality check that randomly passes or fails to simulate validation.

The tasks run sequentially in the order: extract → transform → load → data_quality_check.

## Data Quality Checks

The data quality check task simulates validation by randomly passing or raising an error to indicate failure. This is a placeholder for real data quality checks, which can be implemented using Great Expectations.

## Great Expectations Integration

The `great_expectations` directory is mounted into the Airflow containers and can be used to define and run data validation suites as part of the pipeline.

## Accessing Airflow UI

Once the services are running, access the Airflow web UI at:

[http://localhost:8088](http://localhost:8088)

Log in with the admin credentials provided above to monitor and manage the DAG runs.

## License

This project is provided as-is without any specific license.
