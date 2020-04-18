import tkinter as tk
from auto_trainer.gui.menu_frame_base import MenuFrameBase
from auto_trainer.gui.pokemon_files.pokemon_file_generator_gui import PokemonFileGeneratorGUI


class PokemonMenuFrame(MenuFrameBase):

    def __init__(self, master, back_action=None):
        super().__init__(master)

        button_width = 20

        self._main_frame = tk.Frame(self)
        self.set_menu_content(self._main_frame)

        self._title_label = tk.Label(self._main_frame, 
            text='Pokemon Files', font=(None, 16))
        self._new_button = tk.Button(self._main_frame, text='New',
            width=button_width, command=self._on_new_pressed)
        self._edit_button = tk.Button(self._main_frame, text='Edit',
            width=button_width)
        self._delete_button = tk.Button(self._main_frame, text='Delete',
            width=button_width)
        self._back_button = tk.Button(self._main_frame, text='Back',
            width=button_width, command=back_action)

        self._title_label.grid(row=0, column=0, pady=3)
        self._new_button.grid(row=1, column=0, pady=3)
        self._edit_button.grid(row=2, column=0, pady=3)
        self._delete_button.grid(row=3, column=0, pady=3)
        self._back_button.grid(row=4, column=0, pady=3)
    
    def _on_new_pressed(self):
        file_gen_gui = PokemonFileGeneratorGUI()
        file_gen_gui.mainloop()