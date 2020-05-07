from auto_trainer.menu_controller import MenuController


class PokemonOptionsMenuController(MenuController):

    def __init__(self, pokemon, in_combat):
        super().__init__(4 + (0 if in_combat 
            else len(pokemon.get_ooc_moves())))
        self._ooc_moves = pokemon.get_ooc_moves()
        self._in_combat = in_combat
    
    def select_move(self, move):
        if move in self._ooc_moves:
            index = 1 + self._ooc_moves.index(move)
            self.select_index(index)
        else:
            raise ValueError('Invalid move: ' + move)
    
