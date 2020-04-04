import tkinter as tk
from auto_trainer.gui.next_back_frame import NextBackFrame
from auto_trainer.gui.move_rotation_frame import MoveRotationFrame


class PokemonMoveRotationComponent(NextBackFrame):

    def __init__(self, master, moves, exit_next_action=None, 
        exit_back_action=None, quit_action=None):
        super().__init__(master, 
            exit_next_action=exit_next_action,
            exit_back_action=exit_back_action,
            quit_action=quit_action)
        
        self._rotation_frame = MoveRotationFrame(self, moves)
        self.set_content(self._rotation_frame)
    
    def _on_next_pressed(self):
        self._exit_next_action()
    
    def _on_back_pressed(self):
        self._exit_back_action()