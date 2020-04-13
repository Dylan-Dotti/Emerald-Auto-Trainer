import tkinter as tk
import tkinter.ttk as ttk
import auto_trainer.services.pokemon_moves_data_service as pmds
from auto_trainer.gui.multistage_frame import MultiStageFrame
from auto_trainer.gui.pokemon_sprite_component import PokemonSpriteComponent


class PokemonLearnMovesComponent(MultiStageFrame):

    def __init__(self, master, pkm_data,
        exit_next_action=None, exit_prev_action=None):
        super().__init__(master, exit_next_action=exit_next_action,
            exit_prev_action=exit_prev_action)
        
        evos = pkm_data['evolutions']
        evo_stage_names = [pkm_data['name']] + [
            evo['name'] for evo in evos]
        for i, name in enumerate(evo_stage_names):
            stage_display = PokemonSpriteComponent(self, name)
            stage_display.grid(row=i + 1, column=0)

    
    def next_stage(self):
        pass

    def prev_stage(self):
        pass

    def can_transition_next(self):
        return True

    def can_transition_prev(self):
        return True
