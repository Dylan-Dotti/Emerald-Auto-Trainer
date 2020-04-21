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


def get_area_level_range(area, enc_method='walk'):
    encounter_details_map = get_area_encounters(area)
    if len(encounter_details_map) == 0:
        return None
    min_levels = []
    max_levels = []
    for details in encounter_details_map.values():
        level_ranges = [(d['min_level'], d['max_level'])
            for d in details if d['method']['name'] == enc_method]
        min_levels.extend([lrange[0] for lrange in level_ranges])
        max_levels.extend([lrange[1] for lrange in level_ranges])
    return min(min_levels), max(max_levels)


if __name__ == '__main__':
    print(get_area_level_range('hoenn-route-102-area'))
