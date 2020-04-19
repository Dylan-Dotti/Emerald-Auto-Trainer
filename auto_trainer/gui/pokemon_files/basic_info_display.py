import tkinter as tk
from auto_trainer.gui.pokemon_files.pokemon_sprite_component import PokemonSpriteComponent


class BasicInfoDisplay(tk.Frame):

    def __init__(self, master, pkm_data):
        super().__init__(master)

        sprite_component = PokemonSpriteComponent(self, pkm_data['name'])
        sprite_component.grid(row=0, column=0)

        level_gender_frame = tk.Frame(self)
        level_gender_frame.grid(row=1, column=0)

        level_label = tk.Label(level_gender_frame, text=pkm_data['level'])
        gender_label = tk.Label(level_gender_frame, text=pkm_data['gender'])
        level_label.grid(row=0, column=0)
        gender_label.grid(row=0, column=1)

        moves_frame_outer = tk.Frame(self)
        moves_frame_outer.grid(row=2, column=0)

        moves_title_label = tk.Label(moves_frame_outer, text='Moves:')
        moves_title_label.grid(row=0, column=0)

        moves_frame_inner = tk.Frame(moves_frame_outer)
        moves_frame_inner.grid(row=1, column=0)

        move_labels = [tk.Label(moves_frame_inner, text=m.title())
            for m in pkm_data['moves']]
        move_labels[0].grid(row=0, column=0)
        move_labels[1].grid(row=0, column=1)
        move_labels[2].grid(row=1, column=0)
        move_labels[3].grid(row=1, column=1)
