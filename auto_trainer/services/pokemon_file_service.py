import auto_trainer.services.pokemon_data_directory_service as pdds
import os


def get_file_name_id_pairs():
    file_dir = pdds.get_pokemon_data_directory()
    file_names = [f.replace('.json', '') for f in os.listdir(file_dir)]
    name_id_pairs = [tuple(f.split('_')) for f in file_names]
    return name_id_pairs
    