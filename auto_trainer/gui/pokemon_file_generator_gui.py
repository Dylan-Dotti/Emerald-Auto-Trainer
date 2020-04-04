import tkinter as tk
import tkinter.ttk as ttk
import os
import auto_trainer.services.pokemon_data_directory_service as pdds
import auto_trainer.services.json_data_service as jds
from auto_trainer.gui.emerald_gui_window_base import EmeraldGUIWindowBase
from auto_trainer.gui.pokemon_basic_info_component import PokemonBasicInfoComponent
from auto_trainer.gui.pokemon_evolution_component import PokemonEvolutionComponent
from auto_trainer.gui.pokemon_move_rotation_component import PokemonMoveRotationComponent
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
            self.main_frame,
            exit_next_action=self._on_component_exit_next,
            exit_back_action=None, quit_action=self.quit)
        self.rotation_component = None
        self.evolution_select_frame = None
        self.basic_info_frame.grid(row=0, column=0)
        self.resizable(False, False)

    def _on_component_exit_next(self):
        print('component exit next')
        self.frame_index += 1
        if self.frame_index == 1:
            self.pkm_data.update(self.basic_info_frame.get_pokemon_data())
            self.basic_info_frame.grid_forget()
            self.rotation_component = PokemonMoveRotationComponent(
                self.main_frame, self.pkm_data['moves'],
                exit_next_action=self._on_component_exit_next,
                exit_back_action=self._on_component_exit_back,
                quit_action=self.quit)
            self.rotation_component.grid(row=0, column=0)
        elif self.frame_index == 2:
            self.rotation_component.grid_forget()
            self.evolution_select_frame = PokemonEvolutionComponent(
                self.main_frame, self.pkm_data,
                exit_next_action=self._on_component_exit_next,
                exit_back_action=self._on_component_exit_back,
                quit_action=self.quit)
            self.evolution_select_frame.grid(row=0, column=0)
        elif self.frame_index == 2:
            self.pkm_data['evolutions'] = (
                self.evolution_select_frame.get_evolutions())
            self._generate_pokemon_file()
            self.quit()
        else:
            self._generate_pokemon_file()
            self.quit()

    def _on_component_exit_back(self):
        self.frame_index -= 1
        if self.frame_index == 0:
            self.evolution_select_frame.grid_forget()
            self.basic_info_frame.grid(row=0, column=0)
    
    def _generate_pokemon_file(self):
        pkm_name = self.pkm_data['name']
        direct = pdds.get_pokemon_data_directory()
        id_index = 0
        while (os.path.exists(
            '%s%s_%i.json' % (direct, pkm_name, id_index)) or
            os.path.exists(
                '%s%s_%i.json' % (direct, pkm_name, id_index))):
            id_index += 1
        file_name = '%s%s_%i.json' % (direct, pkm_name, id_index)
        jds.save_data(file_name, self.pkm_data)
        print('Created file:', file_name)
