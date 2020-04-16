import tkinter as tk
import tkinter.ttk as ttk
import os
import auto_trainer.services.pokemon_data_directory_service as pdds
import auto_trainer.services.json_data_service as jds
from auto_trainer.gui.emerald_gui_window_base import EmeraldGUIWindowBase
from auto_trainer.gui.next_back_frame import NextBackFrame
from auto_trainer.gui.pokemon_files.pokemon_basic_info_component import PokemonBasicInfoComponent
from auto_trainer.gui.pokemon_files.pokemon_evolution_component import PokemonEvolutionComponent
from auto_trainer.gui.pokemon_files.pokemon_learn_moves_component import PokemonLearnMovesComponent
from auto_trainer.gui.pokemon_files.pokemon_move_rotation_component import PokemonMoveRotationComponent
from auto_trainer.gui.pokemon_files.pokemon_name_component import PokemonNameComponent
from auto_trainer.gui.emerald_gui_toplevel_base import EmeraldGUIToplevelBase
from auto_trainer.gui.next_back_buttons_group import NextBackButtonsGroup
from auto_trainer.gui.updatable_component import UpdatableComponent
from auto_trainer.gui.pokemon_files.pokemon_sprite_component import PokemonSpriteComponent


class PokemonFileGeneratorGUI(EmeraldGUIToplevelBase, UpdatableComponent):

    def __init__(self):
        super().__init__()
        self.frame_index = 0
        self.pkm_data = {}

        self._main_frame = NextBackFrame(self,
            exit_next_action=self._on_component_exit_next,
            exit_back_action=self._on_component_exit_back,
            quit_action=self.destroy)
        self.main_frame = tk.Frame(self)
        self._main_frame.grid(row=0, column=0, padx=25, pady=15)

        self.basic_info_frame = PokemonBasicInfoComponent(
            self._main_frame,
            exit_next_action=self._on_component_exit_next,
            exit_prev_action=None)
        self.rotation_component = None
        self.evolution_select_frame = None
        self.learn_moves_frame = None
        #self.basic_info_frame.grid(row=0, column=0)
        self._main_frame.set_content(self.basic_info_frame)
        self.resizable(False, False)
    
    def time_update(self, delta_time):
        self._main_frame.time_update(delta_time)

    def _on_component_exit_next(self):
        print('component exit next')
        self.frame_index += 1
        if self.frame_index == 1:
            self.pkm_data.update(self.basic_info_frame.get_pokemon_data())
            self.rotation_component = PokemonMoveRotationComponent(
                self._main_frame, self.pkm_data['moves'],
                exit_next_action=self._on_component_exit_next,
                exit_prev_action=self._on_component_exit_back,
                combo_style='G.TCombobox')
            self._main_frame.set_content(self.rotation_component)
        elif self.frame_index == 2:
            self.pkm_data['move_priority'] = (
                self.rotation_component.get_data())
            self.evolution_select_frame = PokemonEvolutionComponent(
                self._main_frame, self.pkm_data,
                exit_next_action=self._on_component_exit_next,
                exit_prev_action=self._on_component_exit_back)
            self._main_frame.set_content(self.evolution_select_frame)
        elif self.frame_index == 3:
            self.pkm_data['evolutions'] = (
                self.evolution_select_frame.get_evolutions())
            self.learn_moves_frame = PokemonLearnMovesComponent(
                self._main_frame, self.pkm_data,
                exit_next_action=self._on_component_exit_next,
                exit_prev_action=self._on_component_exit_back)
            self._main_frame.set_content(self.learn_moves_frame)
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
