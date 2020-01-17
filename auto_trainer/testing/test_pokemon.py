import pokemon_party as party

def test_get_move_sequence(index, num_moves):
    active_pkm = party.get_pokemon(index)
    print('%s move sequence: ' % active_pkm.get_name())
    print(active_pkm.get_move_sequence(num_moves))


if __name__ == '__main__':
    test_get_move_sequence(3, 5)