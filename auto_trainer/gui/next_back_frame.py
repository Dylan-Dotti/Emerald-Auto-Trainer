import tkinter as tk
from auto_trainer.gui.next_back_buttons_group import NextBackButtonsGroup


class NextBackFrame(tk.Frame):
    def __init__(self):
        super().__init__()
        self._content_frame = None
        self._buttons_group = NextBackButtonsGroup(self)
        self._buttons_group.grid(row=1, column=0)
    
    def set_content_frame(self, content_frame):
        if self._content_frame is not None:
            self._content_frame.grid_forget()
        self._content_frame = content_frame
        if self._content_frame is not None:
            self._content_frame.grid(row=0, column=0)