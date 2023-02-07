import tkinter as tk
import assets.style as style

from database.raw import RawSQL
from tkinter.ttk import Treeview


class WindowRawList(tk.Frame):

    def __init__(self, frame_options, main_window):
        tk.Frame.__init__(self, frame_options)
        self.main_window = main_window

        image_back = tk.PhotoImage(file=r"assets/back_to_menu.png")
        button_menu = tk.Button(self, image=image_back, command=lambda: main_window.show_menu(self),
                                bd=0, highlightthickness=0)
        button_menu.image = image_back
        button_menu.grid(column=0, row=0, sticky='w', padx=(25, 25), pady=(25, 25))

        tk.Label(self, text='CSSP - Metarial List', font=style.title_font).grid(column=1, row=0, sticky='ew')

        image_food = tk.PhotoImage(file=r"assets/add_raw.png")
        button_food = tk.Button(self, image=image_food, command=lambda: main_window.show_raw_add(self),
                                bd=0, highlightthickness=0)
        button_food.image = image_food
        button_food.grid(column=2, row=0, sticky='e', padx=(25, 25), pady=(25, 25))

        table = Treeview(self)
        table['columns'] = ('ID', 'name', 'storage_expiration_date', 'description', 'code')
        table.column('#0', width=0, stretch=tk.NO)
        table.column('ID', width=50)
        table.column('code', width=100)
        table.heading('ID', text='ID')
        table.heading('name', text='Name')
        table.heading('storage_expiration_date', text='Expiration Date')
        table.heading('description', text='Description')
        table.heading('code', text='Barcode')
        table.grid(row=1, column=0, columnspan=3, sticky='ew', padx=(25, 25), pady=(0, 25))

        rawSQL = RawSQL()
        raws = rawSQL.GetAll()

        for raw in raws: #data view in table
            table.insert(parent='', index='end',
                              values=(
                                  raw.id.get(),
                                  raw.name.get(),
                                  raw.storage_expiration_date.get(),
                                  raw.description.get(),
                                  raw.storage_code.get()
                              ))

        table.bind("<Double-1>", self.RawDetail)  #Double mouse click function bind

    def RawDetail(self, event):
        focus_item = event.widget.focus()
        if focus_item:
            item = event.widget.item(focus_item)
            values = item['values']
            raw_id = str(values[0])
            self.main_window.show_raw_detail(raw_id, self)
        return
