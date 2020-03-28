import tkinter as tk

import auto_trainer.gui.window_config.screenshot_display as ssd
import auto_trainer.gui.window_config.sliders_display as sd
import auto_trainer.gui.window_config.window_config_side_bar as sb
import auto_trainer.services.config_settings_data_service as csds
import auto_trainer.services.image_directory_service as ids
import auto_trainer.game_window_grid as gwg
import auto_trainer.keyboard_controller as kc
import auto_trainer.window_controller as wc
import auto_trainer.vision_agent as va


class WindowConfigGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Window Configuration')
        self.iconbitmap(ids.get_emerald_icon_direct())

        self._ss_display = ssd.ScreenshotDisplay(self, None)

        self._side_bar = tk.Frame(self)
        self._side_bar.grid(row=0, column=1)

        self._slider_frame = sd.SlidersDisplay(self._side_bar,
            self.crop_ss_from_sliders)
        border_mods = csds.get_win_border_mods('game')
        for k, v in border_mods.items():
            self._slider_frame.set_slider_value(k, abs(v))
        self._slider_frame.grid(row=0, column=0, padx=20, pady=20)

        self._ss_button = tk.Button(self._side_bar, 
            text='New Screenshot', command=self.on_ss_button_pressed)
        self._ss_button.grid(row=1, column=0, pady=(10, 0))

        self._cancel_confirm_group = tk.Frame(self._side_bar)
        self._cancel_confirm_group.grid(row=2, column=0, pady=10)
    
        self._cancel_button = tk.Button(self._cancel_confirm_group,
            text='Cancel', command=self.on_cancel_button_pressed)
        self._cancel_button.grid(row=0, column=0, padx=(0, 5))

        self._confirm_button = tk.Button(self._cancel_confirm_group, 
            text='Confirm', #state=tk.DISABLED,
            command=self.on_confirm_button_pressed)
        self._confirm_button.grid(row=0, column=1, padx=(5, 0))

        self.resizable(False, False)
        self.display_window_ss()
    
    def take_window_ss(self):
        wc.set_window_foreground_and_resize()
        window_ss = va.screenshot(region=wc.get_window_rect())
        kc.alt_tab()
        return window_ss
    
    def display_window_ss(self):
        ss = self.take_window_ss()
        self._ss_display.grid_forget()
        self._ss_display.display_image(ss)
        self._ss_display = ssd.ScreenshotDisplay(self, ss)
        self._ss_display.grid(row=0, column=0)
    
    def on_ss_button_pressed(self):
        self.display_window_ss()
        self.crop_ss_from_sliders()
    
    def on_confirm_button_pressed(self):
        svals = self._slider_frame.get_slider_values()
        svals['right'] *= -1
        svals['bottom'] *= -1
        csds.set_win_border_mods('game', svals)
        self.destroy()
    
    def on_cancel_button_pressed(self):
        self.destroy()
    
    def crop_ss_from_sliders(self, new_val=None):
        if self._ss_display.has_image():
            svals = self._slider_frame.get_slider_values()
            self._ss_display.crop_image(svals['top'], svals['bottom'],
                svals['left'], svals['right'])