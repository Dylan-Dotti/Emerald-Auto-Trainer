import tkinter as tk
from tkinter import ttk
import auto_trainer.services.pokemon_evolution_data_service as peds
from auto_trainer.gui.pokemon_level_component import PokemonLevelComponent
from auto_trainer.gui.pokemon_sprite_component import PokemonSpriteComponent


class EvolutionSelectionComponent(tk.Frame):

    def __init__(self, master, pkm_data, combo_style=None):
        super().__init__(master)
        self.evolutions = {name : conds for name, conds in 
            peds.get_level_up_evolutions(pkm_data['name'])}
        self.pkm_data = pkm_data
        self.evo_data = {}
        self.combo_style = combo_style
        if len(self.evolutions) > 0:
            self.prompt_label = tk.Label(self, text='Select Evolution:')
            self.evo_cbox = ttk.Combobox(self, state='readonly',
                values=['None'] + [evo_name.capitalize() for 
                    evo_name in self.evolutions],
                width=11, style=combo_style)
            self.evo_cbox.bind('<<ComboboxSelected>>',
                lambda e: self._on_evo_selected())
            self.sprite_display = None
            self.level_cbox = None
            self.prompt_label.grid(row=0, column=0)
            self.evo_cbox.grid(row=1, column=0)
    
    def get_evo_data(self):
        return self.evo_data
    
    def _on_evo_selected(self):
        self.prompt_label.grid_forget()
        if self.evo_cbox.get() == 'None':
            if self.sprite_display is not None:
                self.sprite_display.grid_forget()
            if self.level_cbox is not None:
                self.level_cbox.grid_forget()
            return
        evo_name = self.evo_cbox.get().lower()
        self.sprite_display = PokemonSpriteComponent(
            self, evo_name)
        min_evo_lvl = self.pkm_data['level'] + 1
        conditions = self.evolutions[evo_name]
        if 'min_level' in conditions:
            min_evo_lvl = max(
                min_evo_lvl, conditions['min_level'])
        self.level_cbox = PokemonLevelComponent(self,
            min_lvl=min_evo_lvl, 
            combo_style=self.combo_style)
        self.sprite_display.grid(row=0, column=0)
        self.level_cbox.grid(row=2, column=0)
