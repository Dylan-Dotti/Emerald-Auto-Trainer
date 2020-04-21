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


def get_area_encounters(area_name, version='emerald'):
    area_data = phs.get_one('location-area', area_name)
    encounters = area_data['pokemon_encounters']
    encounter_details_map = {}
    for enc in encounters:
        name = enc['pokemon']['name']
        version_details = enc['version_details']
        for details in version_details:
            if details['version']['name'] == version:
                enc_details = details['encounter_details']
                encounter_details_map[name] = enc_details
                break
    return encounter_details_map

def get_area_level_range(area):
    pass


if __name__ == '__main__':
    print(get_area_encounters('hoenn-route-102-area').keys())
