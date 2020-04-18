import tkinter as tk
from auto_trainer.gui.config_menu_frame import ConfigMenuFrame
from auto_trainer.gui.menu_frame_base import MenuFrameBase
from auto_trainer.gui.pokemon_menu_frame import PokemonMenuFrame


class MainMenuFrame(MenuFrameBase):

    def __init__(self, master, exit_action=None):
        super().__init__(master)

        self._main_frame = tk.Frame(self)
        self.set_menu_content(self._main_frame)

        title_label = tk.Label(self._main_frame, 
            text='Emerald Auto-Trainer', font=(None, 16))
        title_label.grid(row=0, column=0, pady=5)

        run_button = tk.Button(self._main_frame, 
            text='Run...', width=20)
        run_button.grid(row=1, column=0, pady=3)

        pokemon_button = tk.Button(self._main_frame, text='Pokemon...', 
            width=20, command=self._on_pokemon_pressed)
        pokemon_button.grid(row=2, column=0, pady=3)

        config_button = tk.Button(self._main_frame, text='Configure...', 
            width=20, command=self._on_configure_pressed)
        config_button.grid(row=3, column=0, pady=3)

        exit_button = tk.Button(self._main_frame, text='Exit', 
            width=20, command=exit_action)
        exit_button.grid(row=10, column=0, pady=3)
    
    def _on_pokemon_pressed(self):
        pokemon_menu_frame = PokemonMenuFrame(self,
            back_action=self._on_subframe_back)
        self.set_menu_content(pokemon_menu_frame)

    def _on_configure_pressed(self):
        config_menu_frame = ConfigMenuFrame(self,
            back_action=self._on_subframe_back)
        self.set_menu_content(config_menu_frame)
    
    def _on_subframe_back(self):
        self.set_menu_content(self._main_frame)