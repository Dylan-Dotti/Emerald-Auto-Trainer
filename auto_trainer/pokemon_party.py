import auto_trainer.pokemon
import auto_trainer.services.pokemon_party_data_service as ppds


def get_all_pokemon():
    return _party_pokemon


def get_pokemon(index):
    return _party_pokemon[index]


def get_active_pokemon():
    return _party_pokemon[0]


def get_pokemon_with_move(move_name):
    for pkm in get_all_pokemon():
        if move_name in pkm.get_moves():
            return pkm


def get_index_of(pokemon):
    for i, pkm in enumerate(get_all_pokemon()):
        if pkm == pokemon:
            return i


def party_size():
    return len(_party_pokemon)


def switch_pokemon(index_1, index_2):
    temp = _party_pokemon[index_1]
    _party_pokemon[index_1] = _party_pokemon[index_2]
    _party_pokemon[index_2] = temp


def increment_pokemon_level(p_index):
    _party_pokemon[p_index].increment_level()


def to_dictionary():
    return [pkm.to_dictionary() for pkm in _party_pokemon]


def save_party():
    ppds.save_party(to_dictionary())


def __load_party():
    print('loading party from file')
    return ppds.load_party()


_party_pokemon = __load_party()
