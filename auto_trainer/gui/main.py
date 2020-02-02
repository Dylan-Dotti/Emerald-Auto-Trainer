import tkinter as tk
from sprite_display import SpriteDisplay


def display_image(rt, name_entry):
    #name_entry.config(state='disabled')
    for name in [None, name_entry.get()]:
        sp_display = SpriteDisplay(rt, name)
        sp_display.grid(row=1, column=0, rowspan=1, columnspan=2)


root = tk.Tk()
root.title('Emerald Auto-Trainer')
root.iconbitmap('emerald.ico')
frame = tk.Frame(root, relief=tk.SUNKEN)
frame.pack(padx=25, pady=25)

name_label = tk.Label(frame, text='Pokemon Species Name:')
name_text = tk.Entry(frame)
print('Name:', name_text.get())
submit_button = tk.Button(frame, text='Submit', padx=2, pady=2,
    command=lambda: display_image(frame, name_text))
cancel_button = tk.Button(frame, text='Cancel', command=root.quit)

name_label.grid(row=0, column=0)
name_text.grid(row=0, column=1)
submit_button.grid(row=2, column=0)
cancel_button.grid(row=2, column=1)
frame.rowconfigure(1, minsize=100)
root.mainloop()