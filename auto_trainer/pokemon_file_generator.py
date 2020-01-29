import services.json_data_service as jds
import services.pokemon_evolution_data_service as peds
import services.pokemon_moves_data_service as pmds
import services.pokemon_data_service as pds
import os
from evolution import Evolution


def create_pokemon_from_input():
    print('Creating new pokemon file:')
    # get identifying data
    p_name = input('Enter the pokemon species name: ').lower()
    p_lvl = _get_level_input('Enter the pokemon\'s level: ')
    p_gender = input('Enter the pokemon\'s gender (male/female): ').lower()
    print('Enter the pokemon\'s moves, separated by a comma:')
    p_moves = input().split(',')
    print('')
    # get evolutions
    evolutions = []
    next_evo = _get_next_evolution(p_name, p_lvl)
    while next_evo is not None:
        evolutions.append(next_evo)
        next_evo = _get_next_evolution(
            next_evo.get_after_name(), next_evo.get_evo_level())
    # determine moves to learn leveling up
    moves_to_learn, running_move_pool = _get_level_up_moves_to_learn(
        p_name, p_lvl, p_moves, False,
        max_lvl=100 if len(evolutions) == 0 else 
        evolutions[0].get_evo_level())
    for i, evo in enumerate(evolutions):
        print('At level %i, %s will evolve into %s' %
            (evo.get_evo_level(), evo.get_before_name(), 
            evo.get_after_name()))
        mtl, running_move_pool = _get_level_up_moves_to_learn(
            evo.get_after_name(), evo.get_evo_level(), 
            running_move_pool, True, 
            max_lvl=100 if i == len(evolutions) - 1 else
            evolutions[i + 1].get_evo_level())
        moves_to_learn += mtl
    # create file data
    pkm_data = {
        'name': p_name,
        'level': p_lvl,
        'gender': p_gender,
        'moves': p_moves,
        'moves_to_learn': moves_to_learn,
        'evolutions': [evo.to_dictionary() for evo in evolutions]
    }
    _generate_pokemon_file(pkm_data)


def _get_next_evolution(p_name, p_lvl):
    evolutions = peds.get_level_up_evolutions(p_name)
    p_name = p_name.capitalize()
    if p_lvl == 100 or len(evolutions) == 0:
        return None
    # choose to evolve or not
    if len(evolutions) == 1:
        evo_name = evolutions[0][0]
        if _get_y_or_n_input(
            '%s can evolve into %s, do you want ' % 
            (p_name, evo_name.capitalize()) +
            'this evolution to occur (y/n)? ') == 'y':
            next_evo = evolutions[0]
        else:
            next_evo = None
    # choose from selection of evolutions
    elif len(evolutions) > 1:
        evos = {evo[0] : evo[1] for evo in evolutions}
        print('%s can evolve into one of these forms while leveling up:' % 
            p_name, ', '.join(evos.keys()))
        next_evo_name = _get_choice_from_options(
            'Which form should %s evolve into (or "none")? ' % p_name,
            list(evos.keys()) + ['none'])
        next_evo = ((next_evo_name, evos[next_evo_name]) if 
            next_evo_name != 'none' else None)
    # get desired level for evolution
    if next_evo is None:
        return None
    next_evo_name, next_evo_conditions = next_evo
    # if level is specified
    if 'min_level' in next_evo_conditions:
        evo_level = max(next_evo_conditions['min_level'], p_lvl + 1)
        print('The earliest level that this evolution can ' + 
            'occur at is %i' % evo_level)
        if _get_y_or_n_input('Do you want %s ' % p_name + 
            'to evolve at this level (y/n)? ') == 'n':
            evo_level = _get_level_input('Which level should ' +
            '%s evolve at? ' % p_name, min_lvl=evo_level)
    # level not specified - happiness? time of day?
    else:
        print('A minimum level for this evolution is not specified. ' +
            'It is instead determined by special conditions')
        evo_level = _get_level_input('Which level should ' +
            '%s evolve at? ' % p_name, min_lvl=p_lvl + 1)
    return Evolution(p_name.lower(), next_evo_name, 
        evo_level, next_evo_conditions)


def _get_level_up_moves_to_learn(p_name, p_lvl, p_moves, 
    incl_curr_lvl, max_lvl=100):
    level_up_moves = pmds.get_all_level_up_moves(p_name)
    level_up_moves = [(m, l) for (m, l) in level_up_moves
                      if (l >= p_lvl if incl_curr_lvl else l > p_lvl)]
    running_move_pool = [m for m in p_moves]
    moves_to_learn = []
    for mv, lv in level_up_moves:
        if mv not in running_move_pool and lv <= max_lvl:
            if len(running_move_pool) < 4:
                # learn move automatically
                print('At level %i, %s will learn %s\n' %
                    (lv, p_name.capitalize(), mv))
                moves_to_learn.append(
                    {'name': mv, 'level': lv, 'replace': None})
                running_move_pool.append(mv)
            else:
                # choose whether to replace move
                print('At level %s, %s will attempt to learn %s' %
                    (lv, p_name.capitalize(), mv))
                print('The move pool at this level will be:\n')
                for m in running_move_pool:
                    print(m)
                print('')
                if _get_y_or_n_input('Should %s learn %s (y/n)? ' % 
                    (p_name.capitalize(), mv)) == 'y':
                    # replace move in running pool
                    repl_move = _get_choice_from_options(
                        'Which move should be replaced? ', running_move_pool)
                    running_move_pool[running_move_pool.index(repl_move)] = mv
                    moves_to_learn.append(
                        {'name': mv, 'level': lv, 'replace': repl_move})
                print('')
    return moves_to_learn, running_move_pool


def _generate_pokemon_file(pkm_data):
    pkm_name = pkm_data['name']
    id_index = 0
    while (os.path.exists(
        '../data/pokemon/%s_%i.json' % (pkm_name, id_index)) or
        os.path.exists(
            'data/pokemon/%s_%i.json' % (pkm_name, id_index))):
        id_index += 1
    file_name = 'data/pokemon/%s_%i.json' % (pkm_name, id_index)
    try:
        jds.save_data(file_name, pkm_data)
    except FileNotFoundError:
        jds.save_data('../%s' % file_name, pkm_data)
    print('Created file:', file_name)


def _get_y_or_n_input(prompt):
    return _get_user_input(prompt,
        lambda x: x in ['y', 'n'], 
        'please answer with "y" or "n"')


def _get_choice_from_options(prompt, options,
    err_msg='invalid selection'):
    return _get_user_input(prompt,
        lambda x: x in options, err_msg)


def _get_level_input(prompt, min_lvl=1, max_lvl=100):
    return int(_get_user_input(prompt,
        lambda x: int(x) >= min_lvl and int(x) <= max_lvl,
        'Please enter a level between %i and %i' % (min_lvl, max_lvl)))


def _get_user_input(prompt, validation_func, error_msg):
    while True:
        response = input(prompt).lower()
        if validation_func(response):
            return response
        print(error_msg)


if __name__ == '__main__':
    create_pokemon_from_input()
