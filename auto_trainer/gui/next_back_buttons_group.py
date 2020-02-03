import tkinter as tk


class NextBackButtonsGroup(tk.Frame):

    def __init__(self, master, back_action=None,
        next_action=None, quit_action=None):
        super().__init__(master)
        self._back_button = tk.Button(self, text='Back',
            padx=10, command=back_action)
        self._next_button = tk.Button(self, text='Next',
            padx=10, command=next_action)
        self._quit_button = tk.Button(self, text='Quit',
            padx=10, command=quit_action)
        self._back_button.grid(row=0, column=0, padx=2)
        self._next_button.grid(row=0, column=1, padx=2)
        self._quit_button.grid(row=0, column=2, padx=5)