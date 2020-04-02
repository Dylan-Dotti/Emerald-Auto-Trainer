import tkinter as tk
import auto_trainer.services.pokemon_evolution_data_service as peds
from auto_trainer.gui.evolution_selection_component import EvolutionSelectionComponent
from auto_trainer.gui.evolution_stage_display_component import EvolutionStageDisplayComponent
from auto_trainer.gui.next_back_frame import NextBackFrame
from auto_trainer.gui.pokemon_sprite_component import PokemonSpriteComponent


class PokemonEvolutionComponent(NextBackFrame):

    def __init__(self, master, pkm_data, 
        exit_next_action=None, exit_back_action=None, quit_action=None):
        super().__init__(master,
            exit_next_action=exit_next_action,
            exit_back_action=exit_back_action,
            quit_action=quit_action)
        
        self.evo_data = {}
        self._stage_displays = []
        self._selection_comps = []

        self._upper_frame = tk.Frame(self)
        self.set_content(self._upper_frame)

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
    
    def _on_next_pressed(self):
        if len(self._selection_comps) == 0:
            self._exit_next_action()
        else:
            evo_selection_comp = self._selection_comps[-1]
            if evo_selection_comp.is_valid():
                evo_data = evo_selection_comp.get_evo_data()
                if len(peds.get_level_up_evolutions(evo_data['name'])) == 0:
                    self._exit_next_action()
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

    def _on_back_pressed(self):
        self._exit_back_action()
