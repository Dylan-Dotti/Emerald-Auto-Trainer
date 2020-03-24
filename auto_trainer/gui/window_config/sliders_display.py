import tkinter as tk
import auto_trainer.services.config_settings_data_service as csds

class SlidersDisplay(tk.Frame):

    def __init__(self, master, change_event_handler):
        super().__init__(master)

        self._top_label = tk.Label(self, text='Top:', justify='right')
        self._bottom_label = tk.Label(self, text='Bottom:', justify='right')
        self._left_label = tk.Label(self, text='Left:', justify='right')
        self._right_label = tk.Label(self, text='Right:', justify='right')

        self._top_slider = tk.Scale(self, from_=0, to=100,
            orient=tk.HORIZONTAL, command=change_event_handler)
        self._bottom_slider = tk.Scale(self, from_=0, to=100,
            orient=tk.HORIZONTAL, command=change_event_handler)
        self._left_slider = tk.Scale(self, from_=0, to=100,
            orient=tk.HORIZONTAL, command=change_event_handler)
        self._right_slider = tk.Scale(self, from_=0, to=100,
            orient=tk.HORIZONTAL, command=change_event_handler)
        
        self._top_label.grid(row=0, column=0)
        self._bottom_label.grid(row=1, column=0)
        self._left_label.grid(row=2, column=0)
        self._right_label.grid(row=3, column=0)
        
        self._top_slider.grid(row=0, column=1)
        self._bottom_slider.grid(row=1, column=1)
        self._left_slider.grid(row=2, column=1)
        self._right_slider.grid(row=3, column=1)
    
    def get_slider_names(self):
        return ['top', 'bottom', 'left', 'right']
    
    def get_slider(self, slider_name):
        slider_name = slider_name.lower()
        if slider_name == 'top':
            return self._top_slider
        elif slider_name == 'bottom':
            return self._bottom_slider
        elif slider_name == 'left':
            return self._left_slider
        elif slider_name == 'right':
            return self._right_slider
        else:
            raise ValueError('Invalid slider name')
    
    def get_sliders(self):
        return [self.get_slider(s) for s in self.get_slider_names()]
    
    def get_slider_value(self, slider_name):
        return self.get_slider(slider_name).get()
    
    def get_slider_values(self):
        return {s : self.get_slider_value(s) for
                s in self.get_slider_names()}
    
    def set_slider_value(self, slider_name, new_val):
        self.get_slider(slider_name).set(new_val)
    
    def set_sliders_active(self, active):
        for slider in self.get_sliders():
            slider.config(state=tk.ACTIVE if active else tk.DISABLED)
