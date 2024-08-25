# This class is responsible for talking to the Flight Search API.
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
api_access_token = os.getenv("ACCESS_TOKEN")

class FlightSearch:
    def get_token(self):
        end_point = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": api_key,
            "client_secret": api_secret,
        }
        response = requests.post(url=end_point, headers=header, data=body)
        print(response.text)

    def get_iata_code(self, city_name):
        return "TESTING"