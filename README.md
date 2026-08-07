# KRA-Inspired Tax Data Pipeline

## Project Overview

A Data Engineering portfolio project that simulates a reliable, daily tax-data pipeline for a tax-administration environment.

The pipeline will ingest synthetic tax filings, validate and transform them, and produce analytics-ready reporting data for revenue and filing compliance. Its design is inspired by practices discussed by a KRA data engineer, but it is not an official KRA system.

## Objectives

- Generate realistic but fully synthetic tax-filing data.
- Land incoming data in a raw storage layer without modifying the original files.
- Validate records and identify missing, invalid, duplicate, or suspicious submissions.
- Load valid records into PostgreSQL staging tables.
- Build tested reporting models using dbt.
- Orchestrate a reliable daily T-1 pipeline with Apache Airflow.
- Produce data for revenue, filing-volume, and compliance reporting.
- Ensure that rerunning a pipeline does not duplicate data.

## Synthetic Data Disclaimer

This project uses fabricated data only. It does not use real taxpayer information, KRA credentials, KRA systems, or confidential government data.

## Planned Architecture

```text
Synthetic tax filings
        ↓
MinIO raw-data zone
        ↓
Python validation and cleaning
        ↓
PostgreSQL staging tables
        ↓
dbt reporting models and data tests
        ↓
Airflow-orchestrated daily T-1 workflow
        ↓
Revenue and compliance analytics
```

The T-1 requirement means that each scheduled run processes the previous day’s synthetic submissions and makes reporting data available for the next business day.

## Tech Stack

- Python
- SQL
- PostgreSQL
- MinIO
- dbt
- Apache Airflow
- Docker and Docker Compose
- Git and GitHub

## Expected Outputs

The project will produce analytics-ready tables and SQL queries for:

- Daily declared tax by tax type and reporting period
- Filing volumes by county
- Valid, rejected, and duplicate submission counts
- Records that fail defined data-quality rules
- Synthetic taxpayer filing-compliance summaries
- Pipeline-run audit records, including processed file and row counts

## Skills Demonstrated

- Batch data ingestion and raw-data storage
- Data validation and quality checks
- Incremental and idempotent loading
- Relational data modeling
- dbt transformations and tests
- Airflow task orchestration, retries, and logging
- Clear, modular Python code and SQL
