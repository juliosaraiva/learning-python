from folium import Map, Marker, Popup
from geo import GeoPoint


# Get latitude and longitude values
latitude, longitude = 40.4, -3.7


# Folium Map Instance
madrid = Map(location=[latitude, longitude])

geopoint = GeoPoint(latitude=latitude, longitude=longitude)
popup = Popup(str(geopoint.get_weather()))
popup.add_to(geopoint)
geopoint.add_to(madrid)

# Save the Map instance into a HTML file
madrid.save('map.html')