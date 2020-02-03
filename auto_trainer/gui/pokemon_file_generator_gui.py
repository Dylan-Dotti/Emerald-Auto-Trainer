import tkinter as tk
from auto_trainer.gui.next_back_buttons_group import NextBackButtonsGroup
from auto_trainer.gui.sprite_display import SpriteDisplay
import time


class PokemonFileGeneratorGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Emerald Auto-Trainer')
        self.iconbitmap('emerald.ico')

        self.frame = tk.Frame(self)
        self.frame.rowconfigure(1, minsize=100)
        self.frame.pack(padx=25, pady=15)

        self.name_label = tk.Label(self.frame, text='Pokemon Species Name:')
        self.name_entry = tk.Entry(self.frame)
        self.sprite_display = SpriteDisplay(self.frame, None)
        self.buttons = NextBackButtonsGroup(self.frame,
            next_action=self._on_next_clicked,
            quit_action=self.quit)

        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.sprite_display.grid(row=1, column=0, columnspan=2)
        self.buttons.grid(row=2, column=1, sticky='se')
        self.resizable(False, False)
    
    def _on_next_clicked(self):
        self._display_image()

    def _display_image(self):
        self.sprite_display.grid_forget()
        self.sprite_display = SpriteDisplay(self.frame, self.name_entry.get())
        self.sprite_display.grid(row=1, column=0, rowspan=1, columnspan=2)