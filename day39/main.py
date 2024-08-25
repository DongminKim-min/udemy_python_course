#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint


dm = DataManager()
fs = FlightSearch()

sheet_data = dm.get_data()["prices"]
city_names = [city["city"].lower() for city in sheet_data]
city_rows = [city["id"] for city in sheet_data]
city_row_dict = {key:val for (key, val) in zip(city_names, city_rows)}
dm.city_row_dict = city_row_dict

for city_name in city_names:
     code = fs.get_iata_code(city_name)
     dm.edit_iata_code(city_name, code)

pprint(dm.get_data())
