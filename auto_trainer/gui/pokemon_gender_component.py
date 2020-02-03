import tkinter as tk
from tkinter import ttk
import auto_trainer.services.gender_data_service as gds


class PokemonGenderComponent(tk.Frame):

    def __init__(self, master, pkm_name, combo_style=None):
        super().__init__(master)
        gender_label = tk.Label(self, text='Gender:')
        possible_genders = gds.get_possible_genders(pkm_name)
        gender_combobox = ttk.Combobox(self, state='readonly',
            values=[g.capitalize() for g in possible_genders],
            width=10, style=combo_style)
        if len(possible_genders) == 1:
            gender_combobox.current(0)
            gender_combobox.config(state='disabled')
        gender_label.grid(row=0, column=0)
        gender_combobox.grid(row=0, column=1)