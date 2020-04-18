import tkinter as tk


class MenuFrameBase(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self._content_frame = None
    
    def set_menu_content(self, content, padx=20, pady=20):
        if self._content_frame is not None:
            self._content_frame.pack_forget()
        if content is not None:
            self._content_frame = content
            self._content_frame.pack(padx=padx, pady=pady)

    def _on_subframe_back(self, subframe):
        raise NotImplementedError
        