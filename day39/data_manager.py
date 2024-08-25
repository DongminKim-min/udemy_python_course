# This class is responsible for talking to the Google Sheet.
import requests
import os
from dotenv import load_dotenv

load_dotenv()
sheet_end_point = os.getenv("SHEET_END_POINT")

class DataManager:
    def __int__(self):
        self.lowest_price = ""
        self.city_row_dict = None

    def get_data(self):
        response = requests.get(url=sheet_end_point)
        return response.json()

    def get_city_row(self, city_name:str):
        return self.city_row_dict[city_name]

    def edit_price(self, city_name):
        city_row = self.get_city_row(city_name)
        update = {
            "price": {
                "lowestPrice": self.lowest_price,
            }
        }
        response = requests.put(url=f"{sheet_end_point}/{city_row}", json=update)
        print(response.text)

    def edit_iata_code(self, city_name:str, iata_code:str):
        city_row = self.get_city_row(city_name)
        update = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=f"{sheet_end_point}/{city_row}", json=update)
        print(response.text)