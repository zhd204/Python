import os
import requests
import datetime as dt


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    LOCATION_API_ENDPOINT = "https://tequila-api.kiwi.com/"
    SEARCH_API_ENDPOINT = "https://tequila-api.kiwi.com/v2"

    def __init__(self):
        tequila_api = os.environ.get("TEQUILA_API")
        self.headers = {
            "accept": "application/json",
            "apikey": tequila_api
        }

    def location_query(self, term: str, local="en-US", location_types="city", limit=10, active_only=True, sort="name"):
        location_query_endpoint = f"{self.LOCATION_API_ENDPOINT}locations/query"
        location_query_parameters = {
            "term": term,
            "locale": local,
            "location_types": location_types,
            "limit": limit,
            "active_only": active_only,
            "sort": sort
        }
        response = requests.get(url=location_query_endpoint,
                                params=location_query_parameters, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def flight_basic_search(self, fly_from: str, fly_to: str, max_fly_duration=20,
                            flight_type="oneway", adults_number=2, max_stopovers=2):
        flight_basic_search_endpoint = f"{self.SEARCH_API_ENDPOINT}/search"
        # assumptions to simplify the parameters
        adult_hold_bag = ""
        adult_hand_bag = ""
        for i in range(adults_number):
            adult_hold_bag += f"1,"  # assume 1 hold bags per adult
            adult_hand_bag += f"1,"  # assume 1 hand bag per adult
        adult_hold_bag = adult_hold_bag.strip(",")
        adult_hand_bag = adult_hand_bag.strip(",")

        max_sector_stopovers = max_stopovers  # assume these two parameters are the same

        date_from = dt.datetime.now().strftime("%d/%m/%Y")
        date_to = (dt.datetime.now() + dt.timedelta(days=180)).strftime("%d/%m/%Y")

        flight_basic_search_parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "max_fly_duration": max_fly_duration,
            "flight_type": flight_type,
            "one_for_city": 1,
            "one_per_date": 0,
            "adults": adults_number,
            "selected_cabins": "M",  # M stands for economy class and works when "one_for_city" is set as 1.
            "adult_hold_bag": adult_hold_bag,  # use format x,x,x... e.g 2,1
            "adult_hand_bag": adult_hand_bag,
            "only_working_days": False,
            "only_weekends": False,
            "partner_market": "us",
            "curr": "USD",
            "locale": "en",
            "max_stopovers": max_stopovers,
            "max_sector_stopovers": max_sector_stopovers
        }
        response = requests.get(url=flight_basic_search_endpoint,
                                params=flight_basic_search_parameters, headers=self.headers)
        response.raise_for_status()
        return response.json()


# test = FlightSearch()
# flight_search_result = test.flight_basic_search("airport:IAD,airport:EWR", "city:PAR,city:BJS")
# print(flight_search_result)
# print("-------------------------------------")
# print(flight_search_result.keys())
# print("-------------------------------------")
# print(flight_search_result["data"][0].keys())
