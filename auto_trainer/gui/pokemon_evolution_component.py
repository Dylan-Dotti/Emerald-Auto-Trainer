import tkinter as tk
import auto_trainer.services.pokemon_evolution_data_service as peds
from auto_trainer.gui.evolution_selection_component import EvolutionSelectionComponent
from auto_trainer.gui.evolution_stage_display_component import EvolutionStageDisplayComponent
from auto_trainer.gui.multistage_frame import MultiStageFrame
from auto_trainer.gui.pokemon_sprite_component import PokemonSpriteComponent


class PokemonEvolutionComponent(MultiStageFrame):

    def __init__(self, master, pkm_data, 
        exit_next_action=None, exit_prev_action=None):
        super().__init__(master,
            exit_next_action=exit_next_action,
            exit_prev_action=exit_prev_action)
        
        self.evolutions = []
        self.evo_stage_displays = []
        self.evo_selection_comps = []

        self._content_frame = tk.Frame(self)
        self._content_frame.grid(row=0, column=0)

        original_evo_display = EvolutionStageDisplayComponent(
            self._content_frame, pkm_data['name'], pkm_data['level'])
        self.evo_stage_displays.append(original_evo_display)
        original_evo_display.grid(row=0, column=0, pady=(0, 5))

        if len(peds.get_level_up_evolutions(pkm_data['name'])) == 0:
            self.no_evo_label = tk.Label(self._content_frame,
                text='Pokemon does not\nevolve by leveling')
            self.no_evo_label.grid(row=0, column=1)
        else:
            evo_selection_comp = EvolutionSelectionComponent(
                self._content_frame, pkm_data['name'], pkm_data['level'],
                combo_style='G.TCombobox')
            self.evo_selection_comps.append(evo_selection_comp)
            evo_selection_comp.grid(row=0, column=1)
    
    def get_evolutions(self):
        return [evo_select.get_evo_data() for 
            evo_select in self.evo_selection_comps]
    
    def next_stage(self):
        if len(self.evo_selection_comps) == 0:
            self._exit_next_action()
        else:
            evo_selection_comp = self.evo_selection_comps[-1]
            if evo_selection_comp.is_valid():
                evo_data = evo_selection_comp.get_evo_data()
                self.evolutions
                if len(peds.get_level_up_evolutions(evo_data['name'])) == 0:
                    self._exit_next_action()
                else:
                    stage_display = EvolutionStageDisplayComponent(
                        self._content_frame, evo_data['name'],
                        evo_data['conditions']['level'])
                    self.evo_stage_displays.append(stage_display)
                    current_column = len(self.evo_selection_comps)
                    evo_selection_comp.grid_forget()
                    stage_display.grid(row=0, column=current_column)
                    next_selection_comp = EvolutionSelectionComponent(
                        self._content_frame, evo_data['name'], 
                        evo_data['conditions']['level'], 
                        combo_style='G.TCombobox')
                    self.evo_selection_comps.append(next_selection_comp)
                    next_selection_comp.grid(row=0, column=current_column + 1)

    def prev_stage(self):
        self._exit_prev_action()
    
    def can_transition_next(self):
        return True
    
    def can_transition_prev(self):
        return True
    

