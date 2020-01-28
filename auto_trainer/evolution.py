
class Evolution:

    def __init__(self, before_name, after_name, 
                    evo_level, conditions):
        self._before_name = before_name
        self._after_name = after_name
        self._evo_level = evo_level
        self._conditions = conditions
    
    def __str__(self):
        return str(self.to_dictionary())
    
    def get_before_name(self):
        return self._before_name
    
    def get_after_name(self):
        return self._after_name
    
    def get_evo_level(self):
        return self._evo_level
    
    def get_conditions(self):
        return self._conditions
    
    def requires_happiness(self):
        return 'min_happiness' in self._conditions
    
    def to_dictionary(self):
        return {
            'before_name': self._before_name,
            'after_name': self._after_name,
            'evo_level': self._evo_level,
            'conditions': self._conditions
        }
    
    @staticmethod
    def from_dictionary(evo_dict):
        return Evolution(evo_dict['before_name'],
            evo_dict['after_name'], evo_dict['evo_level'],
            evo_dict['conditions'])
