# Flask API for Dataset Access

This project is a Flask application that exposes a REST API to make a dataset accessible. The dataset is stored in a MySQL database, and the API provides endpoints to retrieve information based on wallet addresses and date ranges.

## Getting Started
Link to dataset: https://drive.google.com/file/d/1YFp7N1pu6KJnf_rAXeBHR0D-xgNybTvq/view?usp=sharing  \
### Prerequisites

- Python 3.x
- MySQL (Or any database of your choice)
- Flask
- SQLAlchemy
### Create table and fill data
In your preferred database add this query to create the dataset table: \
CREATE TABLE dataset ( \
    id SERIAL PRIMARY KEY, \
    date TIMESTAMP, \
    wallet_address VARCHAR(255), \
    point_value FLOAT, \
    year INTEGER, \
    month INTEGER, \
    day INTEGER \
); \

### Filling up the table
Fill upp the table by running the dataFILL.py file \
python dataFILL.py \

### Run the flask app to bring the api live.
Run by writing this code in terminal and press enter. \
python apiBuilder.py \

API Documentation \
Retrieve Dataset \
Endpoint: /api/dataset \

Method: GET \

Parameters: \

wallet_address (String): The wallet address to query. \
from_date (String): The start date of the date range (format: 'YYYY-MM-DD'). \
to_date (String): The end date of the date range (format: 'YYYY-MM-DD'). \

"http://localhost:5000/api/dataset?wallet_address=0x1155b614971f16758c92c4890ed338c9e3ede6b7&from_date=2024-01-29&to_date=2024-02-29" \

Sample response: \
[ \
  { \
    "wallet_address": "0x1155b614971f16758c92c4890ed338c9e3ede6b7", \
    "from_date": "2024-01-29", \
    "to_date": "2024-02-29", \
    "total_points": 123.45 \
  } \
] \


