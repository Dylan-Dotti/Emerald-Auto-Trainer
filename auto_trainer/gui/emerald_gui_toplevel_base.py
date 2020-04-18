import tkinter as tk
import tkinter.ttk as ttk
import auto_trainer.services.image_directory_service as ids


class EmeraldGUIToplevelBase(tk.Toplevel):

    def __init__(self, grab_set=True):
        super().__init__()
        self.title('Emerald Auto-Trainer')
        self.iconbitmap(ids.get_emerald_icon_direct())

        if grab_set:
            self.grab_set()

        style = ttk.Style()
        style.map('G.TCombobox',
            darkcolor=[('pressed', 'green'), ('focus', 'green'),
                ('readonly', 'green')],
            focusfill=[('readonly', 'green'), ('focus', 'green')],
            selectbackground=[('focus', 'green'), ('pressed', 'green'),
                ('readonly', 'green')],
            selectforeground=[('pressed', 'white')],
        )
        self.option_add('*TCombobox*Listbox.selectBackground', 'green')
        self.option_add('*TCombobox*Listbox.highlightcolor', 'green')