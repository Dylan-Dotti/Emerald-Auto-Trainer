import tkinter as tk
import tkinter.ttk as ttk
import auto_trainer.services.pokemon_file_service as pfs
from auto_trainer.gui.emerald_listbox import EmeraldListbox


class PokemonFileSelector(EmeraldListbox):

    def __init__(self, master, selectmode=tk.SINGLE):
        super().__init__(master, selectmode=selectmode)
        for name, ident in pfs.get_file_name_id_pairs():
            self.insert(tk.END, '%s %s' % (name.title(), ident))
    

        