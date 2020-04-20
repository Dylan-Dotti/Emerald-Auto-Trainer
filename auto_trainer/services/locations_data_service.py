import auto_trainer.services.pokeapi_http_service as phs


def get_all_locations():
    locations = phs.get_one('region', 'hoenn')['locations']
    location_names = [l['name'] for l in locations]
    del locations[location_names.index('mirage-forest'):]
    del locations[location_names.index('battle-resort')]
    return [l['name'] for l in locations]


def get_location_areas(location_name):
    locations = get_all_locations()
    location = next((l for l in locations 
        if l['name'] == location_name))
    return location['areas']


def get_area_level_range(area):
    


if __name__ == '__main__':
    print(get_all_locations())
