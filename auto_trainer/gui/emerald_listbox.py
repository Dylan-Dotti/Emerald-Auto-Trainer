import tkinter as tk


class EmeraldListbox(tk.Listbox):

    def __init__(self, master, selectmode=tk.SINGLE):
        super().__init__(master, selectmode=selectmode,
            highlightcolor='green', selectbackground='green', 
            font=(None, 12), width=15, activestyle=None)
    
    def get_values(self):
        return [v.lower() for v in self.get(0, tk.END)]

    def append_item(self, item, title=True):
        self.insert(tk.END, item.title() if title else item)

    def get_selected(self):
        return self.get(self.curselection())
    
    def pop_selected(self):
        return self.pop_index(self.curselection())
    
    def pop_item(self, item):
        print('popping value:', item)
        print('current values:', self.get_values())
        index = self.get_values().index(item)
        return self.pop_index(index)
    
    def pop_index(self, index):
        value = self.get(index)
        self.delete(index)
        return value
