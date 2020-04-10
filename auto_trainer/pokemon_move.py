
class PokemonMove:
    def __init__(self, coords, initial, consecutive, periodic):
        self._coords = coords
        self._initial = initial
        self._consecutive = consecutive
        self._periodic = periodic

    def get_coords(self):
        return self._coords

    def get_initial(self):
        return self._initial

    def get_consecutive(self):
        return self._consecutive

    def get_periodic(self):
        return self._periodic

    def to_dictionary(self):
        return {
            'coords': self._coords,
            'initial': self._initial,
            'consecutive': self._consecutive,
            'periodic': self._periodic
        }

    @staticmethod
    def from_dictionary(move_data):
        return PokemonMove(
            move_data['coords'], move_data['initial'],
            move_data['consecutive'], move_data['periodic'])
