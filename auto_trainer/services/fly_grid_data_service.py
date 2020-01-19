import services.json_data_service as jds


def get_city_coordinates(city_name):
    cities = jds.load_data(
        'data/fly_grid_city_coords.json')
    return cities[city_name]