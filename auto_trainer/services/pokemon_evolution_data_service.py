import auto_trainer.services.pokeapi_http_service as phs
import auto_trainer.services.pokemon_data_service as pds


def get_level_up_evolutions(pkm_name, version='emerald'):
    next_evos = get_next_evolutions(pkm_name, version)
    level_evos = [evo for evo in next_evos if 
        evo['evolution_details'][0]['trigger']['name'] == 'level-up']
    evos_formatted = []
    for evo in level_evos:
        evo_name = evo['species']['name']
        evo_conditions = {k : v for k, v in 
            evo['evolution_details'][0].items() if
            k != 'trigger' and v is not None and 
            v != '' and v != False}
        evos_formatted.append((evo_name, evo_conditions))
    return evos_formatted


def get_next_evolutions(pkm_name, version='emerald'):
    evo_data = _get_evo_chain(pkm_name)
    # find pokemon in chain
    evo_data = _find_pokemon_in_chain_recursive(
        pkm_name, evo_data)
    # return list of evolution data
    return [evo for evo in evo_data['evolves_to']
            if pds.does_pokemon_exist(
                evo['species']['name'], version)]


def evolves_on_level_up(pkm_name, version='emerald'):
    return len(get_level_up_evolutions(pkm_name, version)) > 0


def _find_pokemon_in_chain_recursive(pkm_name, evo_data):
    if evo_data['species']['name'] == pkm_name:
        return evo_data
    for evo in evo_data['evolves_to']:
        search_result = _find_pokemon_in_chain_recursive(
            pkm_name, evo)
        if search_result is not None:
            return search_result
    return None


def _get_evo_chain(pkm_name):
    species_data = phs.get_one('pokemon-species', pkm_name)
    evo_chain_url = species_data['evolution_chain']['url']
    evo_chain_id = phs.get_id(evo_chain_url, 'evolution-chain')
    return phs.get_one('evolution-chain', evo_chain_id)['chain']