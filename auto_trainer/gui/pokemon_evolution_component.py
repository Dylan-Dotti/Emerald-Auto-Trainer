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
        self._stage_displays = []
        self._selection_comps = []

        self._upper_frame = tk.Frame(self)
        self._upper_frame.grid(row=0, column=0)

        original_evo_display = EvolutionStageDisplayComponent(
            self._upper_frame, pkm_data)
        self._stage_displays.append(original_evo_display)
        original_evo_display.grid(row=0, column=0, pady=(0, 5))

        if len(peds.get_level_up_evolutions(pkm_data['name'])) == 0:
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
        if len(self._selection_comps) == 0:
            self.exit_next_action()
        else:
            evo_selection_comp = self._selection_comps[-1]
            if evo_selection_comp.is_valid():
                evo_data = evo_selection_comp.get_evo_data()
                if len(peds.get_level_up_evolutions(evo_data['name'])) == 0:
                    self.exit_next_action()
                else:
                    stage_display = EvolutionStageDisplayComponent(
                        self._upper_frame, evo_data)
                    self._stage_displays.append(stage_display)
                    current_column = len(self._selection_comps)
                    evo_selection_comp.grid_forget()
                    stage_display.grid(row=0, column=current_column)
                    next_selection_comp = EvolutionSelectionComponent(
                        self._upper_frame, evo_data, combo_style='G.TCombobox')
                    self._selection_comps.append(next_selection_comp)
                    next_selection_comp.grid(row=0, column=current_column + 1)

    def _on_back(self):
        self.exit_back_action()
