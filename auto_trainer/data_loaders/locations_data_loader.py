import os
import auto_trainer.services.directory_service as ds
import auto_trainer.services.json_data_service as jds
import auto_trainer.services.locations_data_service as lds
import auto_trainer.services.pokeapi_http_service as phs


def load_locations(version='emerald'):
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
            loc.pop(key)


    areas = []
    for loc in locations:
        area_names = [a['name'] for a in loc['areas']]
        for a_name in area_names:
            area = phs.get_one('location-area', a_name)
            for key in ['encounter_method_rates', 'names']:
                area.pop(key)
            areas.append(area)

    location_file_url = ds.get_data_directory() + 'emerald_locations.json'
    area_file_url = ds.get_data_directory() + 'emerald_areas.json'
    jds.save_data(location_file_url, locations)
    jds.save_data(area_file_url, areas)


if __name__ == '__main__':
    load_locations()