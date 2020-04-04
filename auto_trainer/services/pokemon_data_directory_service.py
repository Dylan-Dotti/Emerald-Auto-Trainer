import auto_trainer.services.directory_service as ds


def get_pokemon_data_directory():
    return ds.get_data_directory() + 'pokemon\\'