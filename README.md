# Flask API for Dataset Access

This project is a Flask application that exposes a REST API to make a dataset accessible. The dataset is stored in a MySQL database, and the API provides endpoints to retrieve information based on wallet addresses and date ranges.

## Getting Started

### Prerequisites

- Python 3.x
- MySQL
- Flask
- SQLAlchemy

Run by writing this code in terminal and press enter.
python apiBuilder.py

API Documentation
Retrieve Dataset
Endpoint: /api/dataset

Method: GET

Parameters:

wallet_address (String): The wallet address to query.
from_date (String): The start date of the date range (format: 'YYYY-MM-DDTHH:MM:SS').
to_date (String): The end date of the date range (format: 'YYYY-MM-DDTHH:MM:SS').

"http://localhost:5000/api/dataset?wallet_address=sample_wallet&from_date=2022-01-01T00:00:00&to_date=2022-02-01T00:00:00"
response: 
[
  {
    "wallet_address": "sample_wallet",
    "from_date": "2022-01-01T00:00:00",
    "to_date": "2022-02-01T00:00:00",
    "total_points": 123.45
  }
]


