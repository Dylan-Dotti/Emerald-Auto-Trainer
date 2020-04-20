import os
import auto_trainer.services.json_data_service as jds
import auto_trainer.services.pokemon_data_directory_service as pdds
from auto_trainer.pokemon import Pokemon


def get_file_name_id_pairs():
    file_dir = pdds.get_pokemon_data_directory()
    file_names = [f.replace('.json', '') for f in os.listdir(file_dir)]
    name_id_pairs = [tuple(f.split('_')) for f in file_names]
    return name_id_pairs


def get_pokemon_file_path(pkm_name, pkm_file_id):
    file_dir = pdds.get_pokemon_data_directory()
    return file_dir + '%s_%s.json' % (pkm_name, pkm_file_id)


def load_pokemon_from_file(pkm_name, pkm_file_id):
    path = get_pokemon_file_path(pkm_name, pkm_file_id)
    pkm_data = jds.load_data(path)
    return Pokemon.from_dictionary(pkm_data)
    