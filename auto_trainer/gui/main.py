import tkinter as tk
from auto_trainer.gui.sprite_display import SpriteDisplay
from auto_trainer.gui.next_back_buttons_group import NextBackButtonsGroup


def display_image(rt, name_entry):
    #name_entry.config(state='disabled')
    for name in [None, name_entry.get()]:
        sp_display = SpriteDisplay(rt, name)
        sp_display.grid(row=1, column=0, rowspan=1, columnspan=2)


root = tk.Tk()
root.title('Emerald Auto-Trainer')
root.iconbitmap('emerald.ico')
frame = tk.Frame(root)
frame.pack(padx=25, pady=15)

name_label = tk.Label(frame, text='Pokemon Species Name:')
name_text = tk.Entry(frame)
buttons = NextBackButtonsGroup(frame,
    next_action=lambda: display_image(frame, name_text),
    quit_action=root.quit)

name_label.grid(row=0, column=0)
name_text.grid(row=0, column=1)
buttons.grid(row=2, column=1, sticky='se')
frame.rowconfigure(1, minsize=100)
root.resizable(False, False)
root.mainloop()