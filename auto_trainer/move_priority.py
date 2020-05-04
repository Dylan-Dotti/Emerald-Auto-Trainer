

class MovePriority:

    # Prio data - list of dictionaries containing:
    #   move: name of move
    #   initial: initial turn
    #   consecutive: num of consecutive uses
    #   periodic: num of turns between uses
    def __init__(self, prio_data):
        self._prio_data = prio_data

    def generate_move_sequence(self, max_num_moves):
        move_sequence = []
        # dict can't be key
        next_move_uses = {self._get_name(move): self._get_initial(move)
                            for move in self._prio_data}
        i_turn = 1
        # initial moves
        for move in self._prio_data:
            if i_turn >= self._get_initial(move):
                for _ in range(self._get_consecutive(move)):
                    move_sequence.append(self._get_name(move))
                    i_turn += 1
                if self._get_periodic(move) is not None:
                    next_move_uses[self._get_name(move)] = (i_turn + 
                        self._get_periodic(move) - 1)
        # check valid initial params
        if len(move_sequence) < len(self._prio_data):
            raise Exception('Invalid initial params for move priority')
        # periodic moves
        periodic_moves = list(filter(
            lambda m: self._get_periodic(m) is not None, self._prio_data))
        # return if no periodic moves
        if len(periodic_moves) == 0:
            return move_sequence[:max_num_moves]
        # add periodic moves
        while len(move_sequence) < max_num_moves:
            for move in periodic_moves:
                if i_turn >= next_move_uses[self._get_name(move)]:
                    for _ in range(self._get_consecutive(move)):
                        move_sequence.append(self._get_name(move))
                        i_turn += 1
                    next_move_uses[self._get_name(move)] = (
                        i_turn + self._get_periodic(move) - 1)
                    break
        return move_sequence[:max_num_moves]
    
    def _get_name(self, move):
        return move['move']
    
    def _get_initial(self, move):
        return move['initial']
    
    def _get_consecutive(self, move):
        return move['consecutive']
    
    def _get_periodic(self, move):
        return move['periodic']