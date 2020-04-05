import tkinter as tk
from auto_trainer.gui.next_back_buttons_group import NextBackButtonsGroup
from auto_trainer.gui.updatable_component import UpdatableComponent


class NextBackFrame(tk.Frame, UpdatableComponent):
    def __init__(self, master, content=None, exit_next_action=None,
        exit_back_action=None, quit_action=None):
        super().__init__(master)
        self._quit_action = quit_action
        self._exit_next_action = exit_next_action
        self._exit_back_action = exit_back_action
        self._content_frame = None
        self._buttons_group = NextBackButtonsGroup(self,
            back_action=self._on_back_pressed,
            next_action=self._on_next_pressed,
            quit_action=quit_action)
        self._buttons_group.grid(row=1, column=0, pady=(15, 0))
    
    def set_content(self, content_frame):
        if self._content_frame is not None:
            self._content_frame.grid_forget()
        self._content_frame = content_frame
        if self._content_frame is not None:
            self._content_frame.grid(row=0, column=0)
    
    def time_update(self, delta_time):
        if self._content_frame is not None:
            self._buttons_group.set_next_button_enabled(
                self._content_frame.can_transition_next())
            self._buttons_group.set_back_button_enabled(
                self._content_frame.can_transition_prev())
    
    def _on_next_pressed(self):
        if self._content_frame is not None:
            self._content_frame.next_stage()

    def _on_back_pressed(self):
        if self._content_frame is not None:
            self._content_frame.prev_stage()

    def set_back_button_enabled(self, enabled):
        self._buttons_group.set_back_button_enabled(enabled)
    
    def set_next_button_enabled(self, enabled):
        self._buttons_group.set_next_button_enabled(enabled)
