import auto_trainer.controllers.overworld_menu_controller as omc
import auto_trainer.pokemon_party as pp
from auto_trainer.controllers.pokemon_menu_controller import PokemonMenuController
from auto_trainer.controllers.pokemon_options_menu_controller import PokemonOptionsMenuController
from auto_trainer.tasks.task import Task


class UseHmTask(Task):

    def __init__(self, hm):
        super().__init__()
        self._hm = hm

    def execute(self):
        hm_pokemon = pp.get_pokemon_with_move(self._hm)
        hm_pokemon_index = pp.get_index_of(hm_pokemon)
        omc.enable_menu()
        omc.select_pokemon_menu()
        pkm_menu_control = PokemonMenuController()
        pkm_menu_control.select_index(hm_pokemon_index)
        pkm_options_control = PokemonOptionsMenuController(
            hm_pokemon, False)
        pkm_options_control.select_move(self._hm)
        omc.set_menu_enabled(False)
