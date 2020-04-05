from auto_trainer.gui.pokemon_file_generator_gui import PokemonFileGeneratorGUI
from tkinter import ttk
import time


def update_loop(last_upd_time):
    gui.time_update(time.time() - last_upd_time)
    upd_time = time.time()
    gui.after(16, lambda: update_loop(upd_time))

gui = PokemonFileGeneratorGUI()
update_loop(time.time())
gui.mainloop()