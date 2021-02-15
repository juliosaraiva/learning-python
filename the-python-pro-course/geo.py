from random import uniform
from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather

class GeoPoint:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def closest_parallel(self):
        return round(self.latitude)

    def get_time(self):
        timezone_str = TimezoneFinder().timezone_at(lat = self.latitude, lng = self.longitude)
        time_now = datetime.now(timezone(timezone_str))
        return time_now

    def get_timezone(self):
        return TimezoneFinder().timezone_at(lat = self.latitude, lng = self.longitude)

    def get_weather(self):
        weather = Weather(apikey='26631f0f41b95fb9f5ac0df9a8f43c92', lat=self.latitude, lon=self.longitude)
        return weather.next_12h_simplified()
    
    @classmethod
    def random(cls):
        latitude = uniform(-90, 90)
        longitude = uniform(-180, 180)
        return cls(latitude=latitude, longitude=longitude)