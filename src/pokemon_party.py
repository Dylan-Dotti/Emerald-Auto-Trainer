import pokemon

def get_party_pokemon():
    return _party_pokemon

def get_active_pokemon():
    return _party_pokemon[0]

def switch_pokemon(index_1, index_2):
    temp = _party_pokemon[index_1]
    _party_pokemon[index_1] = _party_pokemon[index_2]
    _party_pokemon[index_2] = temp

def increment_pokemon_level(p_index):
    _party_pokemon[p_index].increment_level()

_party_pokemon = [
    pokemon.Pokemon('Pidgey', 9, [
        (0, 1), (0, 1), (0, 0), (0, 0), (0, 0), (0, 0)
    ]),
    pokemon.Pokemon('Ralts', 11, [
        (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)
    ]),
    pokemon.Pokemon('Torchic', 12, [
        (1, 0), (1, 1), (1, 1), (1, 1), (1, 1)
    ]),
    pokemon.Pokemon('Mareep', 5, [
        (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
    ])
]