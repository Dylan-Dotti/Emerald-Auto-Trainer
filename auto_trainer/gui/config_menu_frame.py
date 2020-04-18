import tkinter as tk
from auto_trainer.gui.menu_frame_base import MenuFrameBase
from auto_trainer.gui.window_config.window_config_gui import WindowConfigGUI


class ConfigMenuFrame(MenuFrameBase):

    def __init__(self, master, back_action=None):
        super().__init__(master)

        main_frame = tk.Frame(self)
        self.set_menu_content(main_frame)

        title_label = tk.Label(main_frame, text='Configuration',
            font=(None, 16))
        window_button = tk.Button(main_frame, text='Window Configuration',
            width=20, command=self._on_window_pressed)
        back_button = tk.Button(main_frame, text='Back', width=20,
            command=back_action)
        
        title_label.grid(row=0, column=0, pady=5)
        window_button.grid(row=1, column=0, pady=3)
        back_button.grid(row=2, column=0, pady=3)
    
    def _on_window_pressed(self):
        window_config_gui = WindowConfigGUI()
        window_config_gui.mainloop()