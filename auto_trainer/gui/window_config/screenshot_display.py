import tkinter as tk
import auto_trainer.services.config_settings_data_service as csds
from PIL import ImageTk, Image


class ScreenshotDisplay(tk.Frame):

    def __init__(self, master, image):
        super().__init__(master)
        self._image = image
        self.img_label = tk.Label(self)
        self.img_label.grid(row=0, column=0)
        if image is not None:
            self.display_image(image)
    
    def has_image(self):
        return self._image is not None
    
    def display_image(self, image):
        w, h = image.size
        self.columnconfigure(0, minsize=w + 20)
        self.rowconfigure(0, minsize=h + 20)
        self._image = image
        self._reload_image_label(image)
    
    def crop_image(self, crop_t, crop_b, crop_l, crop_r):
        w, h = self._image.size
        image_cropped = self._image.crop((crop_l, crop_t,
            w - crop_r, h - crop_b))
        self._reload_image_label(image_cropped)
    
    def _reload_image_label(self, image):
        img = ImageTk.PhotoImage(image)
        self.img_label.grid_forget()
        self.img_label = tk.Label(self, image=img)
        self.img_label.image = img
        self.img_label.grid(row=0, column=0)
