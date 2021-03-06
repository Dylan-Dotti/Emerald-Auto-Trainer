# class for storing data for a pokemon,
# and for converting to and from dictionaries
import auto_trainer.pokemon_move as pm
import auto_trainer.services.pokemon_moves_data_service as pmds
from auto_trainer.move_priority import MovePriority


class Pokemon:

    def __init__(self, name, level, gender, moves, move_priority,
        evolutions, moves_to_learn):
        self._name = name
        self._level = level
        self._gender = gender
        self._moves = moves
        self._move_priority = move_priority
        self._evolutions = evolutions
        self._moves_to_learn = moves_to_learn

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_level(self):
        return self._level

    def increment_level(self):
        self._level += 1
        print('%s is now level %s' % (self._name, self._level))
    
    def get_moves(self):
        return self._moves
    
    def get_ooc_moves(self):
        return list(filter(
            lambda m: m in pmds.get_ooc_moves(), self._moves))

    def get_move_sequence(self, max_num_moves):
        return self._move_priority.generate_move_sequence(
            max_num_moves)
    
    def get_move_coords(self, move):
        index = self._moves.index(move)
        if index == 0:
            return (0, 0)
        if index == 1:
            return (0, 1)
        if index == 2:
            return (1, 0)
        if index == 3:
            return (1, 1)
        raise ValueError('Invalid index: %s' % index)

    def to_dictionary(self):
        return {
            'name': self._name,
            'level': self._level,
            'move_priority': [move.to_dictionary() 
                for move in self._move_priority]
        }

    @staticmethod
    def from_dictionary(pkm_data):
        return Pokemon(
            pkm_data['name'],
            pkm_data['level'],
            pkm_data['gender'],
            pkm_data['moves'],
            MovePriority(pkm_data['move_priority']),
            pkm_data['evolutions'],
            pkm_data['moves_to_learn']
        )
