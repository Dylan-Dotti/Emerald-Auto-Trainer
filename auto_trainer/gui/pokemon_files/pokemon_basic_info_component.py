import tkinter as tk
from tkinter import ttk
from auto_trainer.gui.navigable_component import NavigableComponent
from auto_trainer.gui.pokemon_files.pokemon_current_moves_component import PokemonCurrentMovesComponent
from auto_trainer.gui.pokemon_files.pokemon_gender_component import PokemonGenderComponent
from auto_trainer.gui.pokemon_files.pokemon_level_component import PokemonLevelComponent
from auto_trainer.gui.pokemon_files.pokemon_name_component import PokemonNameComponent
from auto_trainer.gui.multistage_frame import MultiStageFrame
from auto_trainer.gui.next_back_frame import NextBackFrame
from auto_trainer.gui.pokemon_files.pokemon_sprite_component import PokemonSpriteComponent


class PokemonBasicInfoComponent(MultiStageFrame):

    def __init__(self, master, exit_next_action=None, exit_prev_action=None):
        super().__init__(master, exit_next_action, exit_prev_action)
        self._index = 0

        self.name_component = PokemonNameComponent(self,
            change_event=self._on_name_changed, combo_style='G.TCombobox')
        self.sprite_display = PokemonSpriteComponent(self, None)
        self.gender_component = PokemonGenderComponent(self, None)
        self.level_component = PokemonLevelComponent(self,
            combo_style='G.TCombobox')
        self.curr_moves_component = PokemonCurrentMovesComponent(
            self, combo_style='G.TCombobox')
        self.gender_component.set_active(False)
        self.level_component.set_active(False)
        self.curr_moves_component.set_active(False)
        
        self.rowconfigure(1, minsize=100)
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
            self.sprite_display = PokemonSpriteComponent(self, new_name)
            self.sprite_display.grid(row=1, column=0, columnspan=2)
    
    def next_stage(self):
        if self._index == 0 and self.name_component.is_valid():
            self._index += 1
            self.name_component.set_active(False)
            self._refresh_gender_component(self.name_component.get_name())
            self._refresh_curr_moves_component(self.name_component.get_name())
            self.level_component.set_active(True)
        elif self._index == 1 and self.is_valid():
            self._exit_next_action()

    def prev_stage(self):
        if self._index == 0:
            self._exit_prev_action()
        if self._index == 1:
            self._index -= 1
            self._refresh_gender_component(None)
            self.gender_component.set_active(False)
            self.level_component.set_active(False)
            self.curr_moves_component.set_active(False)
            self._refresh_curr_moves_component(None)
            self.name_component.set_active(True)
    
    def can_transition_next(self):
        if self._index == 0:
            return self.name_component.is_valid()
        else:
            return True
    
    def can_transition_prev(self):
        return self._index > 0 or self._exit_prev_action != None
    
    def _refresh_gender_component(self, pkm_name):
        self.gender_component.grid_forget()
        self.gender_component = PokemonGenderComponent(
            self, pkm_name, combo_style='G.TCombobox')
        self.gender_component.grid(row=2, column=0, padx=(0, 5))
    
    def _refresh_curr_moves_component(self, pkm_name):
        self.curr_moves_component.grid_forget()
        self.curr_moves_component = PokemonCurrentMovesComponent(
            self, pkm_name=pkm_name, 
            combo_style='G.TCombobox')
        self.curr_moves_component.grid(row=3, column=0, 
            columnspan=2, pady=(15, 0))