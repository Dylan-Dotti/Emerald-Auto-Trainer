import services.json_data_service as jds
from city import City


def get_all_cities():
    cities = jds.load_data(_cities_data_url)['cities']
    return [City.from_dictionary(c) for c in cities]


def get_city(city_name):
    for city in get_all_cities():
        if city.get_name() == city_name:
            return city
    return None


_cities_data_url = 'data/city_coords.json'
