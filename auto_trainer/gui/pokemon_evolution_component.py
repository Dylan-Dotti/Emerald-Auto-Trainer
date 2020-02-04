import tkinter as tk
from auto_trainer.gui.pokemon_sprite_component import PokemonSpriteComponent


class PokemonEvolutionComponent(tk.Frame):

    def __init__(self, master, pkm_data):
        super().__init__(master)
        self.sprite_display = PokemonSpriteComponent(
            self, pkm_data['name'])
        self.name_label = tk.Label(self, 
            text=pkm_data['name'].capitalize())
        self.level_label = tk.Label(self,
            text='Lv: ' + str(pkm_data['level']))
        self.sprite_display.grid(row=0, column=0)
        self.name_label.grid(row=1, column=0)
        self.level_label.grid(row=2, column=0)
