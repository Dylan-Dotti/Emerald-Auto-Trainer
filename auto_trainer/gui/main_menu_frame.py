import tkinter as tk
from auto_trainer.gui.pokemon_files.pokemon_file_generator_gui import PokemonFileGeneratorGUI


class MainMenuFrame(tk.Frame):

    def __init__(self, master, exit_action=None):
        super().__init__(master)
        title_label = tk.Label(self, text='Emerald Auto-Trainer',
            font=(None, 16))
        title_label.grid(row=0, column=0, pady=5)

        run_button = tk.Button(self, text='Run...', width=20)
        run_button.grid(row=1, column=0, pady=3)

        pokemon_button = tk.Button(self, text='Pokemon...', 
            width=20, command=self._on_pokemon_pressed)
        pokemon_button.grid(row=2, column=0, pady=3)

        config_button = tk.Button(self, text='Configure...', width=20)
        config_button.grid(row=3, column=0, pady=3)

        exit_button = tk.Button(self, text='Exit', 
            width=20, command=exit_action)
        exit_button.grid(row=10, column=0, pady=3)
    
    def _on_pokemon_pressed(self):
        pkm_gui = PokemonFileGeneratorGUI()
        pkm_gui.grab_set()
        pkm_gui.mainloop()