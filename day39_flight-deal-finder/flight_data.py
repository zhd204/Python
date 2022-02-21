class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self, flights: dict):
        self.flight_search_summary = {}
        for flight in flights["data"]:
            airlines = "airlines " + " ".join(flight["airlines"])
            local_departure = flight["local_departure"].split("T")[0]
            local_arrival = flight["local_arrival"].split("T")[0]
            self.flight_search_summary[flight["cityCodeTo"]] = {"flyFrom": flight["flyFrom"], "flyTo": flight["flyTo"],
                                                                "cityFrom": flight["cityFrom"], "cityTo": flight["cityTo"],
                                                                "price": flight["price"], "airlines": airlines,
                                                                "local_departure": local_departure,
                                                                "local_arrival": local_arrival}

    def get_flight_data(self):
        return self.flight_search_summary




