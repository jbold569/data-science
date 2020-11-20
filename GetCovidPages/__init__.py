import logging
import requests

def covid_api(page=1) -> dict:
    return requests.get('https://corona-virus-stats.herokuapp.com/api/v1/cases/countries-search?page={}'.format(page)).json()["data"]

def main(name: str) -> int:
    logging.info("In GetCovidPage")
    return covid_api()["paginationMeta"]["totalPages"]

