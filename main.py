"""
Automated API Health Check: Create User Endpoint with Excel Data Integration

This script reads user data (name and job) from an Excel file (`data.xlsx`) and sends POST requests
to the "Create User" API endpoint on `https://reqres.in/api/users`. It validates the API responses
and prints the results for each request.

Usage:
1. Prepare an Excel file (`data.xlsx`) with columns: 'name' and 'job'.
2. Run the script. It will read the data, send requests, and display the API responses.

Example Excel Data:
| name          | job              |
|---------------|------------------|
| John Doe      | Software Engineer|
| Jane Smith    | Data Scientist   |

Example Output:
Request 1: Status Code = 201
Response Content: {"name": "John Doe", "job": "Software Engineer", "id": "123", "createdAt": "2024-04-01T12:34:56.789Z"}
Request 1 was successful!

Dependencies:
- pandas: To read the Excel file.
- requests: To send HTTP requests to the API.

Install dependencies:
pip install pandas requests openpyxl

Author: Amin Rezaei
Email: amin.rezaei@ieee.org
Date: March 10, 2025
"""

import requests
import pandas as pd

# Read the Excel file
df = pd.read_excel('data.xlsx')

# Correct API endpoint
url = 'https://reqres.in/api/users'

index: int

# Loop through each row in the Excel file
for index, row in df.iterrows():
    # Create the payload for the API request
    payload = {
        'name': row['name'],
        'job': row['job']
    }

    # Send the POST request
    response = requests.post(url, json=payload)

    # Debugging: Print status code and response content
    print(f"Request {index + 1}: Status Code = {response.status_code}")
    print(f"Response Content: {response.text}")

    # Check if the request was successful
    if response.status_code == 201:
        print(f"Request {index + 1} was successful!")
        print(response.json())
    else:
        print(f"Request {index + 1} failed with status code {response.status_code}")
