import auto_trainer.services.directory_service as ds
import auto_trainer.services.json_data_service as jds
import auto_trainer.services.pokeapi_http_service as phs

# move functionality to data loader
def get_all_locations(version='emerald'):
    path = ds.get_data_directory() + '%s_locations.json' % version
    locations = jds.load_data(path)
    return locations


def get_areas(location_name, version='emerald'):
    locations = get_all_locations()
    location = next((l for l in locations 
        if l['name'] == location_name))
    area_names = [a['name'] for a in location['areas']]
    areas = [phs.get_one('location-area', an) for an in area_names]
    for area in areas:
        for key in ['encounter_method_rates', 'names']:
            if key in area:
                area.pop(key)
    return areas


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
    print(get_all_locations())
