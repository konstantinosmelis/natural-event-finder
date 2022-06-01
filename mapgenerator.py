import pandas as pd
import folium
import geocoder
import datafinder
import utils

def create_map():
    p = geocoder.ip('me')
    map = folium.Map(location=p.latlng, zoom_start=4, control_scale=True)
    return map


def add_points(map, data):
    for event in data:
        for city in data[event]:
            location = geocoder.geonames(city, key=utils.GEONAMES_KEY)
            if location.geonames_id == None:
                continue
            details = geocoder.geonames(location.geonames_id, method='details', key=utils.GEONAMES_KEY)
            folium.Marker([details.lat, details.lng], popup=str.title(event)).add_to(map)
    map.save("./templates/map.html")


def generate_map(events):
    data = datafinder.get_full_data(events)
    map = create_map()
    add_points(map, data)
