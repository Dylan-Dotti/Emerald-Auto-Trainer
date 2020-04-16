import tkinter as tk
import auto_trainer.services.pokemon_sprite_data_service as psds
from PIL import ImageTk, Image


class PokemonSpriteComponent(tk.Label):

    def __init__(self, master, pkm_name):
        if pkm_name is not None:
            img = Image.open(
                psds.get_front_sprite_direct(pkm_name))
            img.resize((200, 200))
            sprite = ImageTk.PhotoImage(img)
            self.image = sprite
            super().__init__(master, image=sprite)
        else:
            super().__init__(master)

