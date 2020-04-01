import tkinter as tk
from auto_trainer.gui.next_back_buttons_group import NextBackButtonsGroup


class NextBackFrame(tk.Frame):
    def __init__(self, master, quit_action, content=None):
        super().__init__(master)
        self._quit_action = quit_action
        self._content_frame = None
        self._buttons_group = NextBackButtonsGroup(self,
            back_action=self._on_back_pressed,
            next_action=self._on_next_pressed,
            quit_action=quit_action)
        self._buttons_group.grid(row=1, column=0, pady=(15, 0))
    
    def set_content_frame(self, content_frame):
        if self._content_frame is not None:
            self._content_frame.grid_forget()
        self._content_frame = content_frame
        if self._content_frame is not None:
            self._content_frame.grid(row=0, column=0)
    
    def _on_next_pressed(self):
        raise NotImplementedError

    def _on_back_pressed(self):
        raise NotImplementedError
