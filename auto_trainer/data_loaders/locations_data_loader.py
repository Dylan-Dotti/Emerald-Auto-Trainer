import os
import auto_trainer.services.directory_service as ds
import auto_trainer.services.json_data_service as jds
import auto_trainer.services.locations_data_service as lds
import auto_trainer.services.pokeapi_http_service as phs


def load_locations(version='emerald'):
    locations = lds.get_all_locations(version=version)
    areas = [lds.get_all_areas(l_name) for l_name in [
        l['name'] for l in locations]]
    location_file_url = ds.get_data_directory() + 'emerald_locations.json'
    area_file_url = ds.get_data_directory() + 'emerald_areas.json'
    jds.save_data(location_file_url, locations)
    jds.save_data(area_file_url, areas)


if __name__ == '__main__':
    load_locations()