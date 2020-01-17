# class for storing data for a pokemon,
# and for converting to and from dictionaries
import pokemon_move as pm
import move_sequence_generator as msg


class Pokemon:
    def __init__(self, name, level, move_priority):
        self._name = name
        self._level = level
        self._move_priority = move_priority

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_level(self):
        return self._level

    def increment_level(self):
        self._level += 1
        print('%s is now level %s' % (self._name, self._level))

    def get_move_sequence(self, max_num_moves):
        return msg.generate_move_sequence(self._move_priority, max_num_moves)

    def to_dictionary(self):
        return {
            'name': self._name,
            'level': self._level,
            'move_priority': [move.to_dictionary() for move in self._move_priority]
        }

    @staticmethod
    def from_dictionary(pkm_data):
        return Pokemon(
            pkm_data['name'],
            pkm_data['level'],
            [pm.PokemonMove.from_dictionary(move)
             for move in pkm_data['move_priority']]
        )
