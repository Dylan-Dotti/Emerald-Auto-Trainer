import auto_trainer.services.pokeapi_http_service as phs


def does_pokemon_exist(pkm_name, version='emerald'):
    pkm_id = get_pokemon_id_by_name(pkm_name)
    if version == 'emerald':
        return pkm_id <= 386
    return False


def get_all_pokemon_names(version=None):
    results = phs.get_results('pokemon-species')
    if version == 'emerald':
        results = results[:386]
    return [r['name'] for r in results]


def get_pokemon_id_by_name(pkm_name):
    return phs.get_one('pokemon-species', pkm_name)['id']