import tkinter as tk
from tkinter import ttk
from auto_trainer.gui.pokemon_evolution_component import PokemonEvolutionComponent
from auto_trainer.gui.pokemon_gender_component import PokemonGenderComponent
from auto_trainer.gui.pokemon_level_component import PokemonLevelComponent
from auto_trainer.gui.pokemon_name_component import PokemonNameComponent
from auto_trainer.gui.next_back_buttons_group import NextBackButtonsGroup
from auto_trainer.gui.updatable_component import UpdatableComponent
from auto_trainer.gui.pokemon_sprite_component import PokemonSpriteComponent


class PokemonFileGeneratorGUI(tk.Tk, UpdatableComponent):

    def __init__(self):
        super().__init__()
        self.frame_index = 0
        self.title('Emerald Auto-Trainer')
        self.iconbitmap('emerald.ico')

        style = ttk.Style()
        style.map('G.TCombobox',
            darkcolor=[('pressed', 'green'), ('focus', 'green'),
                ('readonly', 'green')],
            focusfill=[('readonly', 'green'), ('focus', 'green')],
            selectbackground=[('focus', 'green'), ('pressed', 'green'),
                ('readonly', 'green')],
            selectforeground=[('pressed', 'white')],
        )
        self.option_add('*TCombobox*Listbox.selectBackground', 'green')
        self.option_add('*TCombobox*Listbox.highlightcolor', 'green')

        self.frame = tk.Frame(self)
        self.frame.rowconfigure(1, minsize=100)
        self.frame.pack(padx=25, pady=15)

        self.pkm_data = {}

        self.name_component = PokemonNameComponent(self.frame,
            change_event=self._on_name_changed, combo_style='G.TCombobox')
        self.sprite_display = PokemonSpriteComponent(self.frame, None)
        self.gender_component = None
        self.level_component = None
        self.buttons = NextBackButtonsGroup(self.frame,
            next_action=self._on_next_clicked,
            back_action=self._on_back_clicked,
            quit_action=self.quit)
        self.buttons.set_back_button_enabled(False)
        
        self.name_component.grid(row=0, column=0, columnspan=2)
        self.sprite_display.grid(row=1, column=0, columnspan=2)
        self.buttons.grid(row=3, column=1, sticky='se')
        self.resizable(False, False)

    def time_update(self, deltatime):
        pass
    
    def _on_next_clicked(self):
        if self.frame_index == 0:
            if self.name_component.is_valid():
                self.frame_index += 1
                self.name_component.set_entry_enabled(False)
                self.gender_component = PokemonGenderComponent(
                    self.frame, self.name_component.get_name(),
                    change_event=self._on_gender_changed,
                    combo_style='G.TCombobox')
                self.level_component = PokemonLevelComponent(
                    self.frame, change_event=self._on_level_changed)
                self.gender_component.grid(row=2, column=0, pady=10)
                self.level_component.grid(row=2, column=1, pady=10)
                self.buttons.set_back_button_enabled(True)
        elif self.frame_index == 1:
            if self.level_component.is_valid():
                self.frame_index += 1
                self._clear_frame()
                evo_component = PokemonEvolutionComponent(
                    self.frame, self.pkm_data)
                evo_component.pack()
    
    def _on_back_clicked(self):
        self.frame_index -= 1
        if self.frame_index == 0:
            self.buttons.set_back_button_enabled(False)
            self.name_component.set_entry_enabled(True)
            self.gender_component.grid_forget()
            self.level_component.grid_forget()
    
    def _on_name_changed(self, new_name):
        self.pkm_data['name'] = new_name
        self._display_image()
    
    def _on_gender_changed(self, new_gender):
        self.pkm_data['gender'] = new_gender
    
    def _on_level_changed(self, new_level):
        self.pkm_data['level'] = new_level

    def _display_image(self):
        self.sprite_display.grid_forget()
        if self.name_component.is_valid():
            self.sprite_display = PokemonSpriteComponent(self.frame, 
                self.name_component.get_name())
            self.sprite_display.grid(row=1, column=0, 
                rowspan=1, columnspan=2)
    
    def _clear_frame(self):
        for s in self.frame.grid_slaves():
            s.grid_forget()