from dotenv import load_dotenv
import os
import requests


load_dotenv()


class DataManager:
    def __init__(self):
        self.SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT_PRICES"]
        self.SHEETY_BASE64_PASS = os.environ["SHEETY_BASE64_PASS_PRICES"]

    def retrieve(self):
        header = {
            "Authorization": f"Basic {self.SHEETY_BASE64_PASS}"
        }
        response = requests.get(url=self.SHEETY_ENDPOINT, headers=header)
        result = response.json()["prices"]
        return result

    def update_code(self, row_id, code):
        header = {
            "Authorization": f"Basic {self.SHEETY_BASE64_PASS}"
        }
        URL_EXTENSION = str(row_id)
        params = {
            "prices": {
                "iataCode": code
            }
        }
        response = requests.put(url=f"{self.SHEETY_ENDPOINT}/{URL_EXTENSION}", json=params, headers=header)

