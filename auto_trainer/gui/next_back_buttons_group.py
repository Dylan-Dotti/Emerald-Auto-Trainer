import tkinter as tk
from tkinter import ttk


class NextBackButtonsGroup(tk.Frame):

    def __init__(self, master, back_action=None,
        next_action=None, quit_action=None):
        super().__init__(master)
        self._back_button = tk.Button(self, text='Back',
            padx=10, command=back_action)
        self._next_button = tk.Button(self, text='Next',
            padx=10, command=next_action)
        self._quit_button = tk.Button(self, text='Quit',
            padx=10, command=quit_action)
        self._back_button.grid(row=0, column=0, padx=2)
        self._next_button.grid(row=0, column=1, padx=2)
        self._quit_button.grid(row=0, column=2, padx=5)
    
    def set_next_button_enabled(self, enabled):
        self._next_button.config(
            state='active' if enabled else 'disabled')

    def set_back_button_enabled(self, enabled):
        self._back_button.config(
            state='active' if enabled else 'disabled')

    def set_quit_button_enabled(self, enabled):
        self._quit_button.config(
            state='active' if enabled else 'disabled')
    
    def update(self):
        print('Buttons update')