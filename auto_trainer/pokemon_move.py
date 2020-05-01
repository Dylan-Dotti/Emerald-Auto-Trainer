
class PokemonMove:
    def __init__(self, name, initial, consecutive, periodic):
        self._name = name
        self._initial = initial
        self._consecutive = consecutive
        self._periodic = periodic
    
    def get_name(self):
        return self._name

    def get_initial(self):
        return self._initial

    def get_consecutive(self):
        return self._consecutive

    def get_periodic(self):
        return self._periodic

    def to_dictionary(self):
        return {
            'move': self._name,
            'initial': self._initial,
            'consecutive': self._consecutive,
            'periodic': self._periodic
        }

    @staticmethod
    def from_dictionary(move_data):
        return PokemonMove(
            move_data['move'], move_data['initial'],
            move_data['consecutive'], move_data['periodic'])
