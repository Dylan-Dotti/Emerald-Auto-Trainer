import tkinter as tk
from tkinter import ttk
from auto_trainer.gui.pokemon_gender_component import PokemonGenderComponent
from auto_trainer.gui.pokemon_level_component import PokemonLevelComponent
from auto_trainer.gui.pokemon_name_component import PokemonNameComponent
from auto_trainer.gui.next_back_buttons_group import NextBackButtonsGroup
from auto_trainer.gui.updatable_component import UpdatableComponent
from auto_trainer.gui.sprite_display import SpriteDisplay


class PokemonFileGeneratorGUI(tk.Tk, UpdatableComponent):

    def __init__(self):
        super().__init__()
        self.title('Emerald Auto-Trainer')
        self.iconbitmap('emerald.ico')

        style = ttk.Style()
        style.map('G.TCombobox',
            #fieldbackground=[('pressed', 'green'), ('focus', 'green'), ('readonly', 'green')],
            focusfill=[('readonly', 'green'), ('focus', 'green')],
            selectbackground=[('focus', 'green'), ('pressed', 'green'), ('readonly', 'green')],
            selectforeground=[('pressed', 'white')],
        )
        self.option_add('*TCombobox*Listbox.selectBackground', 'green')

        self.frame = tk.Frame(self)
        self.frame.rowconfigure(1, minsize=100)
        self.frame.pack(padx=25, pady=15)

        self.name_component = PokemonNameComponent(self.frame,
            change_event=self._display_image, combo_style='G.TCombobox')
        self.sprite_display = SpriteDisplay(self.frame, None)
        self.gender_component = None
        self.level_component = None
        self.buttons = NextBackButtonsGroup(self.frame,
            next_action=self._on_next_clicked,
            back_action=self._on_back_clicked,
            quit_action=self.quit)
        self.buttons.set_back_button_enabled(False)
        
        self.name_component.grid(row=0, column=0, columnspan=2)
        self.sprite_display.grid(row=1, column=0, columnspan=2)
        self.buttons.grid(row=3, column=1, sticky='se')
        self.resizable(False, False)

    def time_update(self, deltatime):
        pass
    
    def _on_next_clicked(self):
        if self.name_component.is_valid():
            self.name_component.set_entry_enabled(False)
            self.gender_component = PokemonGenderComponent(
                self.frame, self.name_component.get_name(),
                combo_style='G.TCombobox')
            self.level_component = PokemonLevelComponent(self.frame)
            self.gender_component.grid(row=2, column=0, pady=10)
            self.level_component.grid(row=2, column=1, pady=10)
            self.buttons.set_back_button_enabled(True)
        else:
            self.sprite_display.grid_forget()
    
    def _on_back_clicked(self):
        self.buttons.set_back_button_enabled(False)
        self.name_component.set_entry_enabled(True)
        self.gender_component.grid_forget()
        self.level_component.grid_forget()

    def _display_image(self):
        self.sprite_display.grid_forget()
        if self.name_component.is_valid():
            self.sprite_display = SpriteDisplay(self.frame, 
                self.name_component.get_name())
            self.sprite_display.grid(row=1, column=0, 
                rowspan=1, columnspan=2)