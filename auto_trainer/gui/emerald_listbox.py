import tkinter as tk


class EmeraldListbox(tk.Listbox):

    def __init__(self, master, selectmode=tk.SINGLE):
        super().__init__(master, selectmode=selectmode,
            highlightcolor='green', selectbackground='green', 
            font=(None, 12), width=15, activestyle=None)
    
    def get_values(self):
        return self.get(0, tk.END)

    def get_selected(self):
        return self.get(self.curselection())
    
    def pop_selected(self):
        return self.pop_index(self.curselection())
    
    def pop_item(self, item):
        values = self.get_values()
        index = values.index(item)
        return self.pop_index(index)
    
    def pop_index(self, index):
        value = self.get(index)
        self.delete(index)
        return value
