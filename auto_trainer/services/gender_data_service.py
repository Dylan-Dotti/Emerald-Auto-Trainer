import auto_trainer.services.pokeapi_http_service as phs


def get_possible_genders(pkm_name):
    genders = [g for g in ['male', 'female'] if 
        can_pokemon_be_gender(pkm_name, g)]
    if len(genders) == 0:
        genders.append('genderless')
    return genders


def can_pokemon_be_gender(pkm_name, gender):
    return pkm_name in _get_all_pokemon_with_gender(gender)


def _get_all_pokemon_with_gender(gender):
    pokemon_list = phs.get_one('gender', gender)['pokemon_species_details']
    return [p['pokemon_species']['name'] for p in pokemon_list]