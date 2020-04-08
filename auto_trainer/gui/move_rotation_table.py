import tkinter as tk
import tkinter.ttk as ttk


class MoveRotationTable(tk.Frame):

    def __init__(self, master, moves, combo_style=None):
        super().__init__(master)
        self._moves = moves
        self._combo_style = combo_style
        self._move_label = tk.Label(self, text='Move')
        self._initial_label = tk.Label(self, text='Initial')
        self._consecutive_label = tk.Label(self, text='Consecutive')
        self._periodic_label = tk.Label(self, text='Periodic')
        self._move_label.grid(row=0, column=0)
        self._initial_label.grid(row=0, column=1)
        self._consecutive_label.grid(row=0, column=2)
        self._periodic_label.grid(row=0, column=3)

        self._rows = []
        self.add_row()
    
    def num_rows(self):
        return len(self._rows)
    
    def add_row(self):
        irow = self.num_rows()
        widgets = self._get_row_widgets(irow)
        widgets['move'].grid(row=irow + 1, column=0)
        widgets['initial'].grid(row=irow + 1, column=1)
        widgets['consecutive'].grid(row=irow + 1, column=2)
        widgets['periodic'].grid(row=irow + 1, column=3)
        widgets['delete'].grid(row=irow + 1, column=4)
        self._rows.append(widgets)

    def remove_row(self, irow):
        widgets = self._rows[irow]
        for widget in widgets.values():
            widget.grid_forget()
        return widgets

    def _on_move_changed(self, irow):
        print('Move %s changed' % (irow + 1))
    
    def _on_delete_pressed(self, irow):
        print('Delete %s' % (irow + 1))
        self.remove_row(irow)

    def _get_row_widgets(self, irow):
        move_cbox = ttk.Combobox(self, values=self._moves, 
            style=self._combo_style, state='readonly',
            width=18)
            #command=lambda e: self._on_move_changed(irow))
        initial_cbox = ttk.Combobox(self,
            values=[i for i in range(1, 31)], state='readonly',
            width=5, style=self._combo_style)
        consecutive_cbox = ttk.Combobox(self,
            values=[i for i in range(1, 31)], state='readonly',
            width=5, style=self._combo_style)
        periodic_cbox = ttk.Combobox(self,
            values=[i for i in range(1, 31)], state='readonly',
            width=5, style=self._combo_style)
        delete_button = tk.Button(self, text='Delete',
            command=lambda: self._on_delete_pressed(irow))
        return {
            'move': move_cbox,
            'initial': initial_cbox,
            'consecutive': consecutive_cbox,
            'periodic': periodic_cbox,
            'delete': delete_button
        }