import tkinter as tk
from tkinter import ttk


class PokemonLevelComponent(tk.Frame):

    def __init__(self, master, change_event=None, 
            select_color='green'):
        super().__init__(master)
        self.level_var = tk.IntVar()
        self.level_label = ttk.Label(self, text='Level:')
        self.level_spinbox = tk.Spinbox(self,
            textvariable=self.level_var,
            values=list(range(1, 101)), width=3,
            selectbackground=select_color)
        self.level_spinbox.delete(0, tk.END)
        self.level_spinbox.insert(0, 5)
        if change_event is not None:
            self.level_var.trace('w',
                lambda i, v, o: change_event(self.get_level()))
        self.level_label.grid(row=0, column=0)
        self.level_spinbox.grid(row=0, column=1)
    
    def get_level(self):
        try:
            return self.level_var.get()
        except tk.TclError:
            return 0
    
    def is_valid(self):
        level = self.get_level()
        return (level != '' and 
            1 <= level and level <= 100)
