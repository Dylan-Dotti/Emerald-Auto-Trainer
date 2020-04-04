import auto_trainer.services.pokeapi_http_service as phs


def get_all_learnable_moves(pkm_id, version='emerald', sort=True):
    moves = [_get_move_name(m) for m in 
        _get_all_learnable_move_data(pkm_id, version=version)]
    if sort:
        moves = sorted(moves)
    return moves


def get_all_level_up_moves(pkm_id, version='emerald', sort=True):
    moves = _get_all_learnable_move_data(pkm_id)
    moves_filtered = []
    for move in moves:
        for version_details in move['version_group_details']:
            if (version_details['version_group']['name'] == version 
                and _is_level_up_move(version_details)):
                moves_filtered.append((move['move']['name'], 
                    get_learn_level(version_details)))
    if sort:
        moves_filtered = sorted(moves_filtered, key=lambda m: m[1])
    return moves_filtered


def get_learn_level(move_version_details):
    return int(move_version_details['level_learned_at'])


def _is_level_up_move(move_version_details):
    return move_version_details['move_learn_method']['name'] == 'level-up'


def _get_version_details(move, version='emerald'):
    for version_details in move['version_group_details']:
        if version_details['version_group']['name'] == 'emerald':
            return version_details
    return None


def _is_move_in_version(move):
    return _get_version_details(move) is not None


def _get_move_name(move):
    return move['move']['name']


def _get_all_learnable_move_data(pkm_id, version='emerald'):
    moves = phs.get_one('pokemon', pkm_id)['moves']
    version_moves = [m for m in moves if _is_move_in_version(m)]
    for m in version_moves:
        m['move']['name'] = m['move']['name'].replace('-', ' ')
    return version_moves


if __name__ == '__main__':
    moves = get_all_level_up_moves('bulbasaur')
    for name, level in moves:
       print(name, ':', level)
    