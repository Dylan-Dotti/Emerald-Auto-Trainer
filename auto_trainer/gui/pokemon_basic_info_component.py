import tkinter as tk
from tkinter import ttk
from auto_trainer.gui.navigable_component import NavigableComponent
from auto_trainer.gui.pokemon_current_moves_component import PokemonCurrentMovesComponent
from auto_trainer.gui.pokemon_gender_component import PokemonGenderComponent
from auto_trainer.gui.pokemon_level_component import PokemonLevelComponent
from auto_trainer.gui.pokemon_name_component import PokemonNameComponent
from auto_trainer.gui.next_back_frame import NextBackFrame
from auto_trainer.gui.pokemon_sprite_component import PokemonSpriteComponent


class PokemonBasicInfoComponent(NextBackFrame):

    def __init__(self, master, exit_next_action=None,
            exit_back_action=None, quit_action=None):
        super().__init__(master,
            exit_next_action=exit_next_action,
            exit_back_action=exit_back_action,
            quit_action=quit_action)
        self._index = 0
        self.upper_frame = tk.Frame(self)
        self.set_content(self.upper_frame)

        self.name_component = PokemonNameComponent(self.upper_frame,
            change_event=self._on_name_changed, combo_style='G.TCombobox')
        self.sprite_display = PokemonSpriteComponent(self.upper_frame, None)
        self.gender_component = PokemonGenderComponent(self.upper_frame, None)
        self.level_component = PokemonLevelComponent(self.upper_frame,
            combo_style='G.TCombobox')
        self.curr_moves_component = PokemonCurrentMovesComponent(
            self.upper_frame, combo_style='G.TCombobox')
        self.gender_component.set_active(False)
        self.level_component.set_active(False)
        self.curr_moves_component.set_active(False)
        self.set_back_button_enabled(exit_back_action != None)
        
        self.upper_frame.rowconfigure(1, minsize=100)
        self.name_component.grid(row=0, column=0, columnspan=2)
        self.sprite_display.grid(row=1, column=0, columnspan=2)
        self.gender_component.grid(row=2, column=0, padx=(0, 5))
        self.level_component.grid(row=2, column=1, padx=(5, 0))
        self.curr_moves_component.grid(row=3, column=0, 
            columnspan=2, pady=(15, 0))
    
    def get_pokemon_data(self):
        return {
            'name': self.name_component.get_name(),
            'level': self.level_component.get_level(),
            'gender': self.gender_component.get_gender(),
            'moves': self.curr_moves_component.get_all_moves()
        }
    
    def is_valid(self):
        return (self.name_component.is_valid() and
            self.gender_component.is_valid() and 
            self.level_component.is_valid() and
            self.curr_moves_component.is_valid())
    
    def _on_name_changed(self, new_name):
        self.sprite_display.grid_forget()
        if self.name_component.is_valid():
            self.sprite_display = PokemonSpriteComponent(
                self.upper_frame, new_name)
            self.sprite_display.grid(row=1, column=0, columnspan=2)
    
    def _on_next_pressed(self):
        print('basic info next')
        if self._index == 0 and self.name_component.is_valid():
            self._index += 1
            self.name_component.set_entry_enabled(False)
            self._refresh_gender_component(self.name_component.get_name())
            self._refresh_curr_moves_component(self.name_component.get_name())
            self.level_component.set_active(True)
            self.set_back_button_enabled(True)
        elif self._index == 1 and self.is_valid():
            self._exit_next_action()

    def _on_back_pressed(self):
        if self._index == 0:
            self._exit_back_action()
        if self._index == 1:
            self._index -= 1
            self._refresh_gender_component(None)
            self._refresh_curr_moves_component(None)
            self.gender_component.set_active(False)
            self.level_component.set_active(False)
            self.curr_moves_component.set_active(False)
            self.name_component.set_entry_enabled(True)
            self.set_back_button_enabled(
                self._exit_back_action != None)
    
    def _refresh_gender_component(self, pkm_name):
        self.gender_component.grid_forget()
        self.gender_component = PokemonGenderComponent(
            self.upper_frame, pkm_name, combo_style='G.TCombobox')
        self.gender_component.grid(row=2, column=0, padx=(0, 5))
    
    def _refresh_curr_moves_component(self, pkm_name):
        self.curr_moves_component.grid_forget()
        self.curr_moves_component = PokemonCurrentMovesComponent(
            self.upper_frame, pkm_name=pkm_name, 
            combo_style='G.TCombobox')
        self.curr_moves_component.grid(row=3, column=0, 
            columnspan=2, pady=(15, 0))