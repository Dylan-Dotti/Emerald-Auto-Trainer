import tkinter as tk
import tkinter.ttk as ttk
from auto_trainer.gui.pokemon_files.move_rotation_table import MoveRotationTable
from auto_trainer.gui.multistage_frame import MultiStageFrame


class PokemonMoveRotationComponent(MultiStageFrame):

    def __init__(self, master, moves, exit_next_action=None, 
        exit_prev_action=None, combo_style=None):
        super().__init__(master, 
            exit_next_action=exit_next_action,
            exit_prev_action=exit_prev_action)
        
        self._title_label = tk.Label(self, 
            text='Create a move priority:')
        self._title_label.grid(row=0, column=0, pady=(0, 15))

        self._rotation_table = MoveRotationTable(self,
            moves, combo_style=combo_style)
        self._rotation_table.grid(row=1, column=0)
    
    def get_data(self):
        return self._rotation_table.get_data()
    
    def next_stage(self):
        self._exit_next_action()
    
    def prev_stage(self):
        self._exit_prev_action()
    
    def can_transition_next(self):
        return True
    
    def can_transition_prev(self):
        return True