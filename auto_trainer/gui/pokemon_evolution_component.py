import tkinter as tk
import auto_trainer.services.pokemon_evolution_data_service as peds
from auto_trainer.gui.evolution_selection_component import EvolutionSelectionComponent
from auto_trainer.gui.evolution_stage_display_component import EvolutionStageDisplayComponent
from auto_trainer.gui.pokemon_sprite_component import PokemonSpriteComponent


class PokemonEvolutionComponent(tk.Frame):

    def __init__(self, master, pkm_data):
        super().__init__(master)
        self.original_evo_display = EvolutionStageDisplayComponent(
            self, pkm_data)
        self.original_evo_display.grid(row=0, column=0, pady=(0, 5))

        if len(peds.get_level_up_evolutions(pkm_data['name'])) == 0:
            self.no_evo_label = tk.Label(self, text='Pokemon does not\nevolve by leveling')
            self.no_evo_label.grid(row=0, column=1)
        else:
            self.next_evo_frame = EvolutionSelectionComponent(
                self, pkm_data, combo_style='G.TCombobox')
            self.next_evo_frame.grid(row=0, column=1)
