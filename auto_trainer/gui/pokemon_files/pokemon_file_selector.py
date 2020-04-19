import tkinter as tk
import tkinter.ttk as ttk
import auto_trainer.services.pokemon_file_service as pfs


class PokemonFileSelector(tk.Listbox):

    def __init__(self, master, selectmode=tk.SINGLE):
        super().__init__(master, selectmode=selectmode,
            highlightcolor='green', selectbackground='green', 
            font=(None, 12), width=15)
        for name, ident in pfs.get_file_name_id_pairs():
            self.insert(tk.END, '%s %s' % (name.title(), ident))
    

        