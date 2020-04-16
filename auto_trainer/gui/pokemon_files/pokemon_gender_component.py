import tkinter as tk
from tkinter import ttk
import auto_trainer.services.gender_data_service as gds


class PokemonGenderComponent(tk.Frame):

    def __init__(self, master, pkm_name, change_event=None, combo_style=None):
        super().__init__(master)
        self.gender_var = tk.StringVar()
        self.gender_label = tk.Label(self, text='Gender:')
        possible_genders = (gds.get_possible_genders(pkm_name) if
            pkm_name is not None else ['male', 'female', 'genderless'])
        self.gender_combobox = ttk.Combobox(self, state='readonly',
            values=[g.capitalize() for g in possible_genders],
            textvariable=self.gender_var, width=10, style=combo_style)
        if len(possible_genders) == 1:
            self.gender_combobox.current(0)
            self.gender_combobox.config(state='disabled')
        if change_event is not None:
            self.gender_var.trace('w', 
                lambda i, v, o: change_event(self.get_gender()))
        self.gender_label.grid(row=0, column=0)
        self.gender_combobox.grid(row=0, column=1)
    
    def get_gender(self):
        return self.gender_combobox.get().lower()
    
    def is_valid(self):
        return self.get_gender() != ''
    
    def is_active(self):
        return (self.gender_label.cget('state') == tk.NORMAL and
            self.gender_combobox.cget('state') == tk.NORMAL)
    
    def set_active(self, active):
        self.gender_label.configure(state='active' 
            if active else 'disabled')
        self.gender_combobox.configure(state='active' 
            if active else 'disabled')