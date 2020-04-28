import tkinter as tk
from auto_trainer.gui.emerald_gui_toplevel_base import EmeraldGUIToplevelBase
from auto_trainer.gui.pokemon_files.pokemon_file_selector import PokemonFileSelector

class PartyConfigWindow(EmeraldGUIToplevelBase):

    def __init__(self):
        super().__init__()

        self._file_selector = PokemonFileSelector(self)
        self._file_selector.grid(row=0, column=0)

        buttons_frame = tk.Frame(self)
        buttons_frame.grid(row=0, column=1, padx=8)

        self._add_button = tk.Button(buttons_frame,
            text='=>', width=8, command=self._on_add_pressed)
        self._add_button.grid(row=0, column=0)

        self._remove_button = tk.Button(buttons_frame, text='<=', 
            width=8, command=self._on_removed_pressed)
        self._remove_button.grid(row=1, column=0)

        self._confirm_button = tk.Button(buttons_frame,
            text='Confirm', width=8, command=self._on_confirm_pressed)
        self._confirm_button.grid(row=2, column=0)

        self._party_lbox = tk.Listbox(self)
        self._party_lbox.grid(row=0, column=2)
    
    def _on_add_pressed(self):
        #print(self._file_selector.get_selected())
        self._party_lbox.insert(tk.END,
            self._file_selector.pop_selected())

    def _on_removed_pressed(self):
        pass

    def _on_confirm_pressed(self):
        pass