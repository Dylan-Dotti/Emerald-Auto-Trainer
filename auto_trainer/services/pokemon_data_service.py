import services.json_data_service as jds


def _create_pokemon_from_input():
    print('Creating new pokemon file:')
    p_name = input('Enter the pokemon species name: ')
    p_lvl = input('Enter the pokemon level: ')
    print('Enter the pokemon\'s moves, separated by a comma:')
    p_moves = input().split(',')
    print(p_name, p_lvl, p_moves)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        if sys.argv[1] == 'create':
            _create_pokemon_from_input()
