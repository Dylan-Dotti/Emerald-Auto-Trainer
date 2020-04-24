import auto_trainer.services.pokeapi_http_service as phs


def get_all_locations(version='emerald'):
    if version == 'emerald':
        region = 'hoenn'
    locations_index = phs.get_one('region', region)['locations']
    location_names = [l['name'] for l in locations_index]
    del location_names[location_names.index('mirage-forest'):]
    location_names = [l for l in location_names if l not in [
        'battle-resort', 'inside-of-truck', 'hoenn-altering-cave',
        'hoenn-safari-zone', 'ss-tidal', 'secret-base', 'sealed-chamber',
        'island-cave', 'desert-ruins', 'mirage-island', 'southern-island',
        'scorched-slab', 'hoenn-battle-tower', 'hoenn-pokemon-league',
        'underwater', 'mt-chimney', 'ancient-tomb', 'team-aqua-hideout',
        'team-magma-hideout', 'sky-pillar']]
    locations = [phs.get_one('location', l) for l in location_names]
    for loc in locations:
        for key in ['names', 'region', 'game_indices']:
            if key in loc:
                loc.pop(key)
    return locations


def get_all_areas(location_name, version='emerald'):
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
    print(get_all_areas('hoenn-route-102'))
