import time
import tkinter as tk
from tkinter import ttk
from auto_trainer.gui.emerald_gui_window_base import EmeraldGUIWindowBase
from auto_trainer.gui.main_menu_frame import MainMenuFrame
from auto_trainer.gui.pokemon_files.pokemon_file_generator_gui import PokemonFileGeneratorGUI


if __name__ == '__main__':

    def update_loop(last_upd_time):
        gui.time_update(time.time() - last_upd_time)
        upd_time = time.time()
        gui.after(16, lambda: update_loop(upd_time))
    
    def on_config_pressed():
        pass
    
    main_gui = EmeraldGUIWindowBase()

    main_frame = MainMenuFrame(main_gui, exit_action=main_gui.destroy)

    gui = None
    
    main_gui.mainloop()
    #gui.mainloop()