import tkinter as tk


class MultiStageFrame(tk.Frame):

    def __init__(self, master, 
        exit_next_action=None, exit_prev_action=None):
        super().__init__(master)
        self._exit_next_action = exit_next_action
        self._exit_prev_action = exit_prev_action
    
    def next_stage(self):
        raise NotImplementedError

    def prev_stage(self):
        raise NotImplementedError

    def can_transition_next(self):
        raise NotImplementedError

    def can_transition_prev(self):
        raise NotImplementedError