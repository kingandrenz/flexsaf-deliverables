# 📘 Python Error Handling & File Tool

## 📌 Overview

This project contains two simple Python scripts that demonstrate
**real-world error handling**, **debugging**, and **logging**.

It covers: - API requests with failure handling\
- File backup with safety checks

------------------------------------------------------------------------

## 📂 Files

-   `api_fetcher.py` → Fetches data from a public API\
-   `file_backup.py` → Copies content from one file to another safely

------------------------------------------------------------------------

## ⚙️ Requirements

-   Python 3.x\
-   `requests` library

Install dependency:

``` bash
pip install requests
```

------------------------------------------------------------------------

## 🚀 Usage

### 1. Run API Fetcher

``` bash
python api_fetcher.py
```

**What it does:** - Sends a request to a public API\
- Handles timeout, connection, and invalid response errors\
- Logs errors to `api_errors.log`

------------------------------------------------------------------------

### 2. Run File Backup Tool

``` bash
python file_backup.py
```

**What it does:** - Prompts for source and destination files\
- Prevents overwriting existing files\
- Handles missing files and permission errors\
- Logs errors to `file_errors.log`

------------------------------------------------------------------------

## 🛠 Features

-   ✅ Print debugging\
-   ✅ try/except/finally error handling\
-   ✅ Custom error messages\
-   ✅ Logging to file\
-   ✅ Safe file operations

------------------------------------------------------------------------

## 📄 Example Logs

-   `api_errors.log`
-   `file_errors.log`

These files store error details for debugging.

------------------------------------------------------------------------

## 🎯 Purpose

This project is designed to demonstrate how to handle **unpredictable
real-world issues** like: - Network failures\
- Invalid data\
- File system errors
- this is in fulfilment of flexsaf weekly delivarbles

------------------------------------------------------------------------

## 👨‍💻 Author

Anthony kanu

