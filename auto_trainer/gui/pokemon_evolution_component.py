import tkinter as tk
import auto_trainer.services.pokemon_evolution_data_service as peds
from auto_trainer.gui.evolution_selection_component import EvolutionSelectionComponent
from auto_trainer.gui.evolution_stage_display_component import EvolutionStageDisplayComponent
from auto_trainer.gui.navigable_component import NavigableComponent
from auto_trainer.gui.pokemon_sprite_component import PokemonSpriteComponent


class PokemonEvolutionComponent(tk.Frame, NavigableComponent):

    def __init__(self, master, pkm_data, exit_next_action=None,
            exit_back_action=None, exit_quit_action=None):
        tk.Frame.__init__(self, master)
        NavigableComponent.__init__(self, self,
            exit_next_action=exit_next_action,
            exit_back_action=exit_back_action,
            exit_quit_action=exit_quit_action)
        
        self.evo_data = {}
        self._num_evos = len(peds.get_level_up_evolutions(pkm_data['name']))
        self._stage_displays = []
        self._selection_comps = []

        self._upper_frame = tk.Frame(self)
        self._upper_frame.grid(row=0, column=0)

        original_evo_display = EvolutionStageDisplayComponent(
            self._upper_frame, pkm_data)
        self._stage_displays.append(original_evo_display)
        original_evo_display.grid(row=0, column=0, pady=(0, 5))
        # self.evo_selection_comp = None

        if self._num_evos == 0:
            self.no_evo_label = tk.Label(self._upper_frame,
                text='Pokemon does not\nevolve by leveling')
            self.no_evo_label.grid(row=0, column=1)
        else:
            evo_selection_comp = EvolutionSelectionComponent(
                self._upper_frame, pkm_data, combo_style='G.TCombobox')
            self._selection_comps.append(evo_selection_comp)
            evo_selection_comp.grid(row=0, column=1)
    
    def get_evo_data(self):
        return self.evo_data
    
    def _on_next(self):
        if len(self._stage_displays) - 1 == self._num_evos:
            self.exit_next_action()
        else:
            pass

    def _on_back(self):
        self.exit_back_action()
