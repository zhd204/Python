import requests
import os
from flight_search import FlightSearch


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    SHEETY_ENDPOINT = "https://api.sheety.co/f7fabb8332b440cfc3ec74a0c6df78d6/flightDeals/prices"

    def __init__(self):
        token = os.environ.get("BEARER_TOKEN")
        self.headers = {
            "Authorization": f"Bearer {token}",  # bearer authentication
            "Content-Type": "application/json"
        }
        get_sheet = requests.get(url=self.SHEETY_ENDPOINT, headers=self.headers)
        get_sheet.raise_for_status()
        self.sheet = get_sheet.json()
        self.city_ls = self.sheet["prices"]
        self.city_count = len(self.city_ls)  # one city per row
        # print(self.city_ls)
        # print(self.city_count)

    def update_single_iataCode(self, row_index):

        location_search = FlightSearch()
        location_data = location_search.location_query(term=self.city_ls[row_index - 2]["city"])
        iata_code = location_data["locations"][0]["code"]
        self.city_ls[row_index - 2]["iataCode"] = iata_code
        contents = {
            "price": {
                "iataCode": iata_code
            }
        }
        edit_sheet = requests.put(url=f"{self.SHEETY_ENDPOINT}/{row_index}", json=contents, headers=self.headers)
        edit_sheet.raise_for_status()
        print(edit_sheet.text)

    def read_destination(self):
        for row_index in range(2, 2 + self.city_count):
            if self.city_ls[row_index - 2]["iataCode"]:
                # print("iataCode is already filled.")
                continue
            else:
                self.update_single_iataCode(row_index)
        return self.city_ls

