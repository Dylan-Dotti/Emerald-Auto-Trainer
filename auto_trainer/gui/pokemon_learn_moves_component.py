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
        
        labels = ['Move', 'Learn', 'Replace']
        for i, label in enumerate(labels):
            tk.Label(self, text=label).grid(row=0, column=i+1)
        
        evos = pkm_data['evolutions']
        evo_stage_names = [pkm_data['name']] + [
            evo['name'] for evo in evos]
        evo_stage_levels = [pkm_data['level']] + [
            evo['conditions']['level'] for evo in evos]
        evo_data = list(zip(evo_stage_names, evo_stage_levels))
        evo_moves = []
        for i in range(len(evo_data)):
            name, level = evo_data[i]
            stage_moves = [m[0].title() for m in pmds.get_all_level_up_moves(
                name, min_lvl=level + 1 if i == 0 else level,
                max_lvl=100 if i == len(evo_data) - 1 else evo_data[i+1][1])]
            evo_moves.append(stage_moves)
        evo_data = list(zip(evo_stage_names, evo_stage_levels, evo_moves))
        for i, (name, level, moves) in enumerate(evo_data):
            stage_display = PokemonSpriteComponent(self, name)
            stage_display.grid(row=i + 1, column=0, rowspan=len(moves))
            for j, move in enumerate(moves):
                move_label = tk.Label(self, text=move)
                move_label.grid(row=i + 1 + j, column=0)
    
    def next_stage(self):
        self._exit_next_action()

    def prev_stage(self):
        self._exit_prev_action()

    def can_transition_next(self):
        return True

    def can_transition_prev(self):
        return True
    
    def _create_row_widgets(self, curr_moves, new_move):
        move_label = tk.Label(self, text=new_move)
        yes_no_cbox = ttk.Combobox(self, values=['Yes', 'No'])
        replace_cbox = ttk.Combobox(self, 
            values=[m.title() for m in curr_moves])
        return move_label, yes_no_cbox, replace_cbox
