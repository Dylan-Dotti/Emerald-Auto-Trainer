import auto_trainer.overworld_menu_controller as omc
import auto_trainer.pokemon_party as pp
from auto_trainer.pokemon_menu_controller import PokemonMenuController
from auto_trainer.pokemon_options_menu_controller import PokemonOptionsMenuController
from auto_trainer.tasks.task import Task

class FlyTask(Task):

    def __init__(self, source_city, destination_city):
        super().__init__()
        self._source = source_city
        self._destination = destination_city
    
    def execute(self):
        fly_pokemon = pp.get_pokemon_with_move('teleport')
        fly_pokemon_index = pp.get_index_of(fly_pokemon)
        omc.select_pokemon_menu()
        pkm_menu_control = PokemonMenuController()
        pkm_menu_control.select_index(fly_pokemon_index)
        pkm_options_control = PokemonOptionsMenuController(
            fly_pokemon, False)
        pkm_options_control.select_move('teleport')
    

if __name__ == '__main__':
    ftask = FlyTask('test', 'test')
    ftask.execute()
