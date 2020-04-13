import tkinter as tk
from auto_trainer.gui.pokemon_sprite_component import PokemonSpriteComponent


class EvolutionStageDisplayComponent(tk.Frame):

    def __init__(self, master, evo_data):
        super().__init__(master)
        sprite_display = PokemonSpriteComponent(
            self, evo_data['name'])
        name_label = tk.Label(self, 
            text=evo_data['name'].capitalize())
        level_label = tk.Label(self,
            text='Lv: ' + str(evo_data['level']))
        sprite_display.grid(row=0, column=0)
        name_label.grid(row=1, column=0)
        level_label.grid(row=2, column=0)