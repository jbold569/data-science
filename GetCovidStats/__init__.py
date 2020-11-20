import logging
import requests
import json
import uuid
from datetime import datetime as dt

def covid_data(page: int):
    resp = requests.get(f'https://corona-virus-stats.herokuapp.com/api/v1/cases/countries-search?page={page}') \
        .json()["data"]
    timestamp = dt.strptime(resp["last_update"], "%b, %d %Y, %H:%M, %Z") \
        .isoformat()
    data = resp["rows"]

    for row in data:
        row.update({"PartitionKey":"covid", "timestamp":timestamp, "RowKey":str(uuid.uuid4())}) 
    return [json.dumps(d) for d in data]

def main(page: int):
    return covid_data(page)
