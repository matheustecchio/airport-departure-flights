import scrapy
import time


class FlightsSpider(scrapy.Spider):
    name            = "flights"
    allowed_domains = ["www.flightaware.com"]
    start_urls      = ["https://www.flightaware.com/live/airport/EICK"]

    def parse(self, response):
        departure_times:list = response.css("#scheduled-board td:nth-child(4) i::text").extract()
        aircraft_models:list = response.css("#scheduled-board .flight-ident+ td a::text").extract()
        airport_IATAs:list   = response.css("#scheduled-board .hint+ span a::text").extract()
        airport_names:list   = response.css("#scheduled-board .hint span::text").extract()
        flight_numbers:list  = response.css("#scheduled-board .flight-ident a::text").extract()
        flight_quantity:int  = len(flight_numbers)
        
        yield {
            "Date": time.strftime("%Y-%m-%d %H:%M:%S")
            }
        
        for flight in range(flight_quantity):
            yield {
                "Departure Time": departure_times[flight][0:5],
                "Aircraft Model": aircraft_models[flight],
                "Airport IATA": airport_IATAs[flight],
                "Airport Name": airport_names[flight],
                "Flight Number": flight_numbers[flight]
            } 