# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

sheet_data = DataManager()
destination_check_list = sheet_data.read_destination()
print(destination_check_list)

city_iataCode_list = [f"city:{entry['iataCode']}" for entry in destination_check_list]
city_string = ",".join(city_iataCode_list)
airport_string = "airport:IAD,airport:EWR"

flight_search = FlightSearch()
flights = flight_search.flight_basic_search(fly_from=airport_string, fly_to=city_string)

flights_data = FlightData(flights)
flight_summary = flights_data.get_flight_data()

flight_found = False
for city in destination_check_list:
    if city["iataCode"] in flight_summary.keys():
        if flight_summary[city["iataCode"]]["price"] <= city["lowestPrice"]:
            message = f"Low price alert! Only ${flight_summary[city['iataCode']]['price']} to fly from " \
                      f"{flight_summary[city['iataCode']]['cityFrom']}-{flight_summary[city['iataCode']]['flyFrom']} to " \
                      f"{flight_summary[city['iataCode']]['cityTo']}-{flight_summary[city['iataCode']]['flyTo']}, from " \
                      f"{flight_summary[city['iataCode']]['local_departure']} to {flight_summary[city['iataCode']]['local_arrival']} " \
                      f"via {flight_summary[city['iataCode']]['airlines']}. "
            flight_found = True
            print(message)
            notification = NotificationManager()
            notification.send_notification(message)

if not flight_found:
    print("Not flight fight")

print(flight_summary)
