import tkinter as tk


class WindowConfigSideBar(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.config(width=100, height=100)#, background='black')
        ss_button = tk.Button(self, text='Take Screenshot')
        #ss_button.grid(row=10, column=0)