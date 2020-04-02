import tkinter as tk
import tkinter.ttk as ttk
import auto_trainer.services.pokemon_moves_data_service as pmds


class PokemonCurrentMovesComponent(tk.Frame):
    def __init__(self, master, pkm_data=None, combo_style=None):
        super().__init__(master)

        self._prompt_label = tk.Label(self, text='Current Moves:')
        self._prompt_label.grid(row=0, column=0, pady=(0, 5))

        self._cbox_frame = tk.Frame(self)
        self._cbox_frame.grid(row=1, column=0)

        moves = [m[0].title() for m in 
            pmds.get_all_level_up_moves('charmander')]
        self._move_0_cbox = ttk.Combobox(self._cbox_frame, 
            state='readonly', values=moves, style=combo_style)
        self._move_1_cbox = ttk.Combobox(self._cbox_frame, 
            state='readonly', values=moves, style=combo_style)
        self._move_2_cbox = ttk.Combobox(self._cbox_frame, 
            state='readonly', values=moves, style=combo_style)
        self._move_3_cbox = ttk.Combobox(self._cbox_frame, 
            state='readonly', values=moves, style=combo_style)
        
        self._move_0_cbox.grid(row=0, column=0)
        self._move_1_cbox.grid(row=0, column=1)
        self._move_2_cbox.grid(row=1, column=0)
        self._move_3_cbox.grid(row=1, column=1)