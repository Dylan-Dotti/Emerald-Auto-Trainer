import pokemon
import pokemon_party_data_service as ppds


def get_party_pokemon():
    global _party_pokemon
    return _party_pokemon


def get_active_pokemon():
    global _party_pokemon
    return _party_pokemon[0]


def switch_pokemon(index_1, index_2):
    global _party_pokemon
    temp = _party_pokemon[index_1]
    _party_pokemon[index_1] = _party_pokemon[index_2]
    _party_pokemon[index_2] = temp


def increment_pokemon_level(p_index):
    global _party_pokemon
    _party_pokemon[p_index].increment_level()


def to_dictionary():
    global _party_pokemon
    pokemon = [pkm.to_dictionary() for pkm in _party_pokemon]
    return {
        'pokemon': pokemon
    }


def save_party():
    ppds.save_party(to_dictionary())


def load_party():
    global _party_pokemon
    print('loading party from file')
    pkm_dict = ppds.load_party()
    party = [pokemon.Pokemon.from_dictionary(
        pkm) for pkm in pkm_dict['pokemon']]
    _party_pokemon = party


# _party_pokemon = [
#    pokemon.Pokemon('Pidgey', 9, [
#        (0, 1), (0, 1), (0, 0), (0, 0), (0, 0), (0, 0)
#    ]),
#    pokemon.Pokemon('Ralts', 11, [
#        (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)
#    ]),
#    pokemon.Pokemon('Torchic', 12, [
#        (1, 0), (1, 1), (1, 1), (1, 1), (1, 1)
#    ]),
#    pokemon.Pokemon('Mareep', 5, [
#        (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
#    ])
# ]
load_party()
print(_party_pokemon)
