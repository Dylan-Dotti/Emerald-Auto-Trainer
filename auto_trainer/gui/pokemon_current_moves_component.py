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

        #moves = [m[0].title() for m in 
        #    pmds.get_all_level_up_moves('charmander')]
        moves = [m['move']['name'].title() for m in
            pmds.get_all_learnable_moves('charmander')]
        self._cboxes = [ttk.Combobox(self._cbox_frame, 
            state='readonly', values=moves, style=combo_style)
            for _ in range(4)]

        self._cboxes[0].bind('<<ComboboxSelected>>',
            lambda e: self._on_move_changed(0))
        self._cboxes[1].bind('<<ComboboxSelected>>',
            lambda e: self._on_move_changed(1))
        self._cboxes[2].bind('<<ComboboxSelected>>',
            lambda e: self._on_move_changed(2))
        self._cboxes[3].bind('<<ComboboxSelected>>',
            lambda e: self._on_move_changed(3))
        
        self._cboxes[0].grid(row=0, column=0)
        self._cboxes[1].grid(row=0, column=1)
        self._cboxes[2].grid(row=1, column=0)
        self._cboxes[3].grid(row=1, column=1)
    
    def get_move(self, move_index):
        return self._cboxes[move_index].get().lower()
    
    def set_move(self, move_index, move):
        self._cboxes[move_index].set(move)
    
    def get_all_moves(self):
        return [self.get_move(i) for i in range(4)]
    
    def _on_move_changed(self, move_index):
        new_move = self.get_move(move_index)
        if new_move != '':
            for i in [x for x in range(4) if x != move_index]:
                if self.get_move(i) == new_move:
                    self.set_move(i, '')