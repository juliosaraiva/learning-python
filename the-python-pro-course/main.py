from folium import Map

latitude = float("40.09")
longitude = float("-3.47")

antipode_latitude = latitude * (-1)

if longitude <= 0:
    antipode_longitude = longitude + 180.0
else:
    antipode_longitude = longitude - 180.0

location = list((antipode_latitude, antipode_longitude))
antipode_map = Map(location=location)
antipode_map.save('map.html')

print(f'Lat: {antipode_latitude}; Log: {antipode_longitude}')
