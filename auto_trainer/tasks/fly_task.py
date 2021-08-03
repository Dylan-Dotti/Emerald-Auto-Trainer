import auto_trainer.controllers.fly_grid_controller as fgc
import auto_trainer.controllers.overworld_menu_controller as omc
import auto_trainer.pokemon_party as pp
import auto_trainer.controllers.time_controller as tc
from auto_trainer.controllers.pokemon_menu_controller import PokemonMenuController
from auto_trainer.controllers.pokemon_options_menu_controller import PokemonOptionsMenuController
from auto_trainer.tasks.task import Task
from auto_trainer.tasks.use_hm_task import UseHmTask


class FlyTask(Task):

    def __init__(self, destination_city):
        super().__init__()
        self._destination = destination_city

    def execute(self):
        UseHmTask('fly').execute()
        tc.wait_for_seconds(1)
        fgc.fly_to_city(self._destination)
        omc.set_menu_enabled(False)
