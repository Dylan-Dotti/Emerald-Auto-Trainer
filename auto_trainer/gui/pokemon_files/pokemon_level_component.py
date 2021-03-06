import tkinter as tk
from tkinter import ttk


class PokemonLevelComponent(tk.Frame):

    def __init__(self, master, change_event=None, min_lvl=1,
            max_lvl=100, default_lvl=5, combo_style=None):
        super().__init__(master)
        self.min_lvl = min_lvl
        self.max_lvl = max_lvl
        self.level_var = tk.IntVar()
        self.level_label = ttk.Label(self, text='Level:')
        self.level_cbox = ttk.Combobox(self,
            textvariable=self.level_var,
            values=list(range(min_lvl, max_lvl + 1)),
            width=3, style=combo_style)
        if change_event is not None:
            self.level_var.trace('w',
                lambda i, v, o: change_event(self.get_level()))
        default_lvl = min(max(default_lvl, min_lvl), max_lvl)
        self.level_cbox.delete(0, tk.END)
        self.level_cbox.insert(0, default_lvl)
        self.level_label.grid(row=0, column=0)
        self.level_cbox.grid(row=0, column=1)
    
    def get_level(self):
        try:
            return self.level_var.get()
        except tk.TclError:
            return 0
    
    def is_valid(self):
        level = self.get_level()
        return (level != '' and 
            self.min_lvl <= level and level <= self.max_lvl)
    
    def is_active(self):
        return (self.level_label.cget('state') == tk.NORMAL and
            self.level_cbox.cget('state') == tk.NORMAL)
    
    def set_active(self, active):
        self.level_label.configure(state='active' 
            if active else 'disabled')
        self.level_cbox.configure(state='active' 
            if active else 'disabled')
