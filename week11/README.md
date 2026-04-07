# Task Logger & Expense Tracker Project

## Overview

This project demonstrates practical Python development skills
including: - Logging user actions with timestamps - Saving data to CSV
and text files - Using external libraries with pip - Performing simple
data analysis with pandas - Exporting Python environment dependencies

The project contains two main scripts.

------------------------------------------------------------------------

## Deliverable 1: Expense Tracker

**File:** `expense_tracker.py`

This program allows users to record expenses. Each expense is saved with
a timestamp and stored in a CSV file.

### Features

-   Records expense description and amount
-   Automatically adds a timestamp using `datetime`
-   Saves data into `expenses.csv`
-   Uses `pandas` to generate summaries

### Example Data Saved

timestamp,description,amount\
2026-04-07 14:20:01,Lunch,2500\
2026-04-07 16:45:11,Transport,1500

### Summary Generated

-   Total amount spent
-   Average expense

------------------------------------------------------------------------

## Deliverable 2: Task Logger

**File:** `task_logger.py`

This script logs user actions into a text file with timestamps.

### Features

-   Records actions performed by the user
-   Adds timestamps automatically
-   Saves logs into `task_log.txt`

### Example Log

2026-04-07 10:15:02 - User opened program\
2026-04-07 10:16:11 - Added new expense\
2026-04-07 10:17:45 - Generated report

------------------------------------------------------------------------

## Python Environment Management

### Install Required Package

``` bash
pip install pandas
```

### Export Dependencies

``` bash
pip freeze > requirements.txt
```

This creates a file listing all installed packages needed to run the
project.

------------------------------------------------------------------------

## Creating a Virtual Environment

Create environment:

``` bash
python -m venv venv
```

Activate:

Windows

``` bash
venv\Scripts\activate
```

Mac/Linux

``` bash
source venv/bin/activate
```

------------------------------------------------------------------------

## Project Folder Structure

    task_logger_project/
    │
    ├── expense_tracker.py
    ├── task_logger.py
    ├── expenses.csv
    ├── task_log.txt
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## Skills Demonstrated

-   Python file handling
-   Working with timestamps (`datetime`)
-   CSV data storage
-   Data analysis using `pandas`
-   Logging user activity
-   Python package management with `pip`
-   Exporting project dependencies

------------------------------------------------------------------------

## Author
Anthony kanu (flexteck)

Python Practice Project in fulfillment of flexsaf weekly deliverables

