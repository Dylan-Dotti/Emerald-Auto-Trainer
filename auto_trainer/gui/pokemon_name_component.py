import tkinter as tk
from tkinter import ttk
import auto_trainer.services.pokemon_data_service as pds


class PokemonNameComponent(tk.Frame):

    def __init__(self, master, change_event=None, combo_style=None):
        super().__init__(master)
        self.name_label = tk.Label(self, text='Pokemon Name:')
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Combobox(self, width=11, height=8,
            textvariable=self.name_var,
            values=[n.capitalize() for n in 
            pds.get_all_pokemon_names('emerald')],
            style=combo_style)
        if change_event is not None:
            self.name_var.trace('w', 
                lambda i, v, o: change_event(self.get_name()))
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
    
    def get_name(self):
        return self.name_entry.get().lower()
    
    def is_valid(self):
        return self.get_name() in pds.get_all_pokemon_names('emerald')
    
    def set_entry_enabled(self, enabled):
        self.name_entry.config(state=(
            'active' if enabled else 'disabled'))
