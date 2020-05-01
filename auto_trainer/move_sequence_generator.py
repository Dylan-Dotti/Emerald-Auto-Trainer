
def generate_move_sequence(move_priority, max_num_moves):
    move_sequence = []
    next_move_uses = {move: move.get_initial()
                        for move in move_priority}
    i_turn = 1
    # initial moves
    for move in move_priority:
        if i_turn >= move.get_initial():
            for _ in range(move.get_consecutive()):
                move_sequence.append(move.get_name())
                i_turn += 1
            if move.get_periodic() is not None:
                next_move_uses[move] = i_turn + move.get_periodic() - 1
    # check valid initial params
    if len(move_sequence) < len(move_priority):
        raise Exception('Invalid initial params for move priority')
    # periodic moves
    periodic_moves = list(filter(
        lambda m: m.get_periodic() is not None, move_priority))
    # return if no periodic moves
    if len(periodic_moves) == 0:
        return move_sequence[:max_num_moves]
    # add periodic moves
    while len(move_sequence) < max_num_moves:
        for move in periodic_moves:
            if i_turn >= next_move_uses[move]:
                for _ in range(move.get_consecutive()):
                    move_sequence.append(move.get_name())
                    i_turn += 1
                next_move_uses[move] = i_turn + move.get_periodic() - 1
                break
    return move_sequence[:max_num_moves]