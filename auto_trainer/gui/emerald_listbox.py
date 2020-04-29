import tkinter as tk


class EmeraldListbox(tk.Listbox):

    def __init__(self, master, selectmode=tk.SINGLE):
        super().__init__(master, selectmode=selectmode,
            highlightcolor='green', selectbackground='green', 
            font=(None, 12), width=15, activestyle=None)

    def get_selected(self):
        return self.get(self.curselection())
    
    def pop_selected(self):
        selected_val = self.get_selected()
        self.delete(self.curselection())
        return selected_val