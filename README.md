# Compliance Data Quality Checker

## Overview

Compliance Data Quality Checker is a Python-based automation tool designed to improve the quality of compliance and risk reporting datasets.

The tool automatically analyzes Excel datasets and identifies common data quality issues such as:

* Duplicate Issue IDs
* Missing Issue IDs
* Missing Owners
* Missing Countries
* Open vs Closed Issue statistics

It also generates exception reports that allow analysts to quickly investigate problematic records.

---

## Features

### Summary Report

Generates a high-level data quality report containing:

* Total Records
* Duplicate Issue Counts
* Missing Value Counts
* Open Issue Counts
* Closed Issue Counts
* Compliance Health Score

### Exception Reporting

Automatically exports:

* Duplicate Records
* Missing Owner Records

These reports help analysts focus on data requiring remediation.

---

## Project Structure

```text
compliance-data-quality-checker/

├── data/
│   └── sample_issues.xlsx

├── reports/
│   ├── quality_report.xlsx
│   ├── duplicate_records.xlsx
│   └── missing_owner_records.xlsx

├── src/
│   ├── __init__.py
│   └── quality_checker.py

├── tests/
│   └── test_quality_checker.py

├── main.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* OpenPyXL

---

## Future Enhancements

* Multi-sheet Excel reporting
* Streamlit web interface
* Interactive dashboards
* Risk scoring enhancements
* Automated email distribution

---

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

Reports will be generated automatically inside the reports folder.
