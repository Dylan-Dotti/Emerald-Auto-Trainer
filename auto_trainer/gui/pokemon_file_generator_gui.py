import tkinter as tk
from tkinter import ttk
from auto_trainer.gui.emerald_gui_window_base import EmeraldGUIWindowBase
from auto_trainer.gui.pokemon_basic_info_component import PokemonBasicInfoComponent
from auto_trainer.gui.pokemon_evolution_component import PokemonEvolutionComponent
from auto_trainer.gui.pokemon_name_component import PokemonNameComponent
from auto_trainer.gui.next_back_buttons_group import NextBackButtonsGroup
from auto_trainer.gui.updatable_component import UpdatableComponent
from auto_trainer.gui.pokemon_sprite_component import PokemonSpriteComponent


class PokemonFileGeneratorGUI(EmeraldGUIWindowBase):

    def __init__(self):
        super().__init__()
        self.frame_index = 0

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=0, column=0, padx=25, pady=15)

        self.pkm_data = {}

        self.basic_info_frame = PokemonBasicInfoComponent(
            self.main_frame, exit_quit_action=self.quit,
            exit_next_action=self._on_component_exit_next,
            exit_back_action=None)
        self.evolution_select_frame = None
        self.basic_info_frame.grid(row=0, column=0)
        self.resizable(False, False)

    def _on_component_exit_next(self):
        print('component exit next')
        self.frame_index += 1
        if self.frame_index == 1:
            for k, v in self.basic_info_frame.get_pokemon_data().items():
                self.pkm_data[k] = v
            self.basic_info_frame.grid_remove()
            self.evolution_select_frame = PokemonEvolutionComponent(
                self.main_frame, self.pkm_data,
                exit_next_action=self._on_component_exit_next, 
                exit_back_action=self._on_component_exit_back,
                exit_quit_action=self.quit)
            self.evolution_select_frame.grid(row=0, column=0)

    def _on_component_exit_back(self):
        self.frame_index -= 1
        if self.frame_index == 0:
            self.evolution_select_frame.grid_remove()
            self.basic_info_frame.grid(row=0, column=0)