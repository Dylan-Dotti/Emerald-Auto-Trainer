import tkinter as tk


class PokemonMenuFrame(tk.Frame):

    def __init__(self, master, back_action=None):
        super().__init__(master)

        button_width = 20

        self._title_label = tk.Label(self, text='Pokemon Files',
            font=(None, 16))
        self._new_button = tk.Button(self, text='New',
            width=button_width)
        self._edit_button = tk.Button(self, text='Edit',
            width=button_width)
        self._delete_button = tk.Button(self, text='Delete',
            width=button_width)
        self._back_button = tk.Button(self, text='Back',
            width=button_width, command=back_action)

        self._title_label.grid(row=0, column=0, pady=3)
        self._new_button.grid(row=1, column=0, pady=3)
        self._edit_button.grid(row=2, column=0, pady=3)
        self._delete_button.grid(row=3, column=0, pady=3)
        self._back_button.grid(row=4, column=0, pady=3)