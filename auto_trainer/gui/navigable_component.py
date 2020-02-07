import tkinter as tk
from auto_trainer.gui.next_back_buttons_group import NextBackButtonsGroup


class NavigableComponent:

    def __init__(self, master, exit_next_action=None,
            exit_back_action=None, exit_quit_action=None,
            padx=0, pady=(15, 0)):
        self.exit_next_action = exit_next_action
        self.exit_back_action = exit_back_action
        self.exit_quit_action = exit_quit_action
        self.upper_frame = tk.Frame(master)
        self.buttons_group = NextBackButtonsGroup(master,
            back_action=self._on_back, next_action=self._on_next,
            quit_action=self._on_quit)
        self.upper_frame.grid(row=0, column=0)
        self.buttons_group.grid(row=1, column=0, padx=padx, pady=pady)
    
    def _on_next(self):
        pass

    def _on_back(self):
        pass

    def _on_quit(self):
        self.exit_quit_action()
    
