import tkinter as tk
import tkinter.ttk as ttk


class MoveRotationFrame(tk.Frame):

    def __init__(self, master, moves, combo_style=None):
        super().__init__(master)

    def _get_move_select_cbox(self, moves):
        cbox = ttk.Combobox(self, values=moves)
        return cbox