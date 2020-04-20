import tkinter as tk
import auto_trainer.services.pokemon_file_service
from auto_trainer.gui.emerald_gui_toplevel_base import EmeraldGUIToplevelBase
from auto_trainer.gui.pokemon_files.basic_info_display import BasicInfoDisplay
from auto_trainer.gui.pokemon_files.pokemon_file_selector import PokemonFileSelector


class FileDeletionWindow(EmeraldGUIToplevelBase):

    def __init__(self):
        super().__init__()

        file_selector = PokemonFileSelector(self)
        basic_info_display = BasicInfoDisplay(self, 'unknown')

        file_selector.grid(row=0, column=0)
        basic_info_display.grid(row=0, column=1)