import requests
from dotenv import load_dotenv
import os
from datetime import date
from dateutil.relativedelta import relativedelta



load_dotenv()

TEQUILA_KEY = os.environ["TEQUILA_KEY"]
TEQUILA_CODE_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"


class FlightSearch:
    def __init__(self):
        self.iata = "Testing"
        self.tomorrow_date = (date.today() + relativedelta(days=+1)).strftime("%d/%m/%Y")
        self.six_month_date = (date.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")

    def get_iata_code(self, city):
        header = {
            "apikey": TEQUILA_KEY
        }
        params = {
            "term": city,
            "locale": "en-US",
            "location_types": "city",
            "limit": 1,
            "active_only": True
        }
        response = requests.get(url=TEQUILA_CODE_ENDPOINT, headers=header, params=params)
        iata_code = response.json()["locations"][0]["code"]
        return iata_code

    def price_search(self, code):
        header = {
            "apikey": TEQUILA_KEY
        }
        params = {
            "fly_from": "SFO",
            "fly_to": code,
            "date_from": self.tomorrow_date,
            "date_to": self.six_month_date,
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 14,
            "flight_type": "round",
            "adults": 1,
            "sort": "price",
            "curr": "USD",
            "limit": 1
        }
        response = requests.get(url=TEQUILA_SEARCH_ENDPOINT, params=params, headers=header)
        result = response.json()["data"][-1]
        return result


