import auto_trainer.services.directory_service as ds
import auto_trainer.services.json_data_service as jds
import auto_trainer.services.pokeapi_http_service as phs


def get_all_locations(version='emerald'):
    path = ds.get_data_directory() + '%s_locations.json' % version
    locations = jds.load_data(path)
    return locations


def get_areas(location_name, version='emerald'):
    path = ds.get_data_directory() + '%s_areas.json' % version
    areas = jds.load_data(path)
    areas_filtered = list(filter(
        lambda a: a['location'] == location_name, areas))
    return areas_filtered


def get_area(area_name):
    path = ds.get_data_directory() + 'emerald_areas.json'
    areas = jds.load_data(path)
    for a in areas:
        if a['name'] == area_name:
            return a
    raise ValueError('Invalid area name: %s' % area_name)


def get_area_encounters(area_name, enc_method='walk', version='emerald'):
    area = get_area(area_name)
    encounters = area['pokemon_encounters']
    encounter_details_map = {}
    for enc in encounters:
        details = enc['encounter_details']
        details = list(filter(
            lambda d: d['method'] == enc_method, details))
        if len(details) > 0:
            encounter_details_map[enc['pokemon']] = details
    return encounter_details_map


def get_area_level_range(area, enc_method='walk'):
    encounter_details_map = get_area_encounters(area)
    if len(encounter_details_map) == 0:
        return None
    min_levels = []
    max_levels = []
    for details in encounter_details_map.values():
        level_ranges = [(d['min_level'], d['max_level'])
            for d in details if d['method'] == enc_method]
        min_levels.extend([lrange[0] for lrange in level_ranges])
        max_levels.extend([lrange[1] for lrange in level_ranges])
    return min(min_levels), max(max_levels)


if __name__ == '__main__':
    print(get_area_level_range('petalburg-city-area'))
