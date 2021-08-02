import auto_trainer.controllers.fly_grid_controller as fgc
import auto_trainer.controllers.overworld_menu_controller as omc
import auto_trainer.pokemon_party as pp
from auto_trainer.controllers.pokemon_menu_controller import PokemonMenuController
from auto_trainer.controllers.pokemon_options_menu_controller import PokemonOptionsMenuController
from auto_trainer.tasks.task import Task
import time


class FlyTask(Task):

    def __init__(self, destination_city):
        super().__init__()
        self._destination = destination_city

    def execute(self):
        fly_pokemon = pp.get_pokemon_with_move('fly')
        fly_pokemon_index = pp.get_index_of(fly_pokemon)
        omc.enable_menu()
        omc.select_pokemon_menu()
        pkm_menu_control = PokemonMenuController()
        pkm_menu_control.select_index(fly_pokemon_index)
        pkm_options_control = PokemonOptionsMenuController(
            fly_pokemon, False)
        pkm_options_control.select_move('fly')
        time.sleep(1)
        fgc.fly_to_city(self._destination)
        omc.set_menu_enabled(False)
