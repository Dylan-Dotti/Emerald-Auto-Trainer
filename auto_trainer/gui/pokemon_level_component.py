import tkinter as tk


class PokemonLevelComponent(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.level_label = tk.Label(self, text='Level:')
        self.level_spinbox = tk.Spinbox(self,
            values=list(range(1, 101)), width=3)
        self.level_spinbox.delete(0, tk.END)
        self.level_spinbox.insert(0, 5)
        self.level_label.grid(row=0, column=0)
        self.level_spinbox.grid(row=0, column=1)