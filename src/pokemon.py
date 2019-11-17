
class Pokemon:
    def __init__(self, name, level, move_sequence):
        self._name = name
        self._level = level
        self._move_sequence = move_sequence

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name
    
    def get_level(self):
        return self._level
    
    def increment_level(self):
        self._level += 1
        print('%s is now level %s' % (self._name, self._level))

    def get_move_sequence(self):
        return self._move_sequence
