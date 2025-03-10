# API Health Check

A Python script to automate health checks for the "Create User" API endpoint using data from an Excel file. This tool reads input data (e.g., name, job) from an Excel file, sends POST requests to the API, and validates the responses.

---

## Features
- Reads user data (name and job) from an Excel file (`data.xlsx`).
- Sends POST requests to the "Create User" API endpoint on `https://reqres.in/api/users`.
- Validates API responses and prints results for each request.
- Easy to use and extend for other APIs.

---

## Prerequisites
- Python 3.x
- Libraries: `pandas`, `requests`, `openpyxl`

Install the required libraries using:
```bash
pip install pandas requests openpyxl
