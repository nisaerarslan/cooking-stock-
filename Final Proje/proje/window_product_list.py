import tkinter as tk
import assets.style as style

from database.product import ProductSQL
from tkinter.ttk import Treeview


class WindowProductList(tk.Frame):

    def __init__(self, frame_options, main_window):
        tk.Frame.__init__(self, frame_options)
        self.main_window = main_window

        image_back = tk.PhotoImage(file=r"assets/back_to_menu.png")
        button_menu = tk.Button(self, image=image_back, command=lambda: main_window.show_menu(self),
                                   bd=0, highlightthickness=0)
        button_menu.image = image_back
        button_menu.grid(column=0, row=0, sticky='w', padx=(25, 25), pady=(25, 25))

        tk.Label(self, text='CSSP - Food List', font=style.title_font).grid(column=1, row=0, sticky='ew')

        image_food = tk.PhotoImage(file=r"assets/add_product.png")
        button_food = tk.Button(self, image=image_food, command=lambda: main_window.show_product_add(self),
                                bd=0, highlightthickness=0)
        button_food.image = image_food
        button_food.grid(column=2, row=0, sticky='e', padx=(25, 25), pady=(25, 25))

        table = Treeview(self)
        table['columns'] = ('ID', 'name', 'product_expiration_date', 'description', 'code')
        table.column('#0', width=0, stretch=tk.NO)
        table.column('ID', width=50)
        table.column('code', width=100)
        table.heading('ID', text='ID')
        table.heading('name', text='Foods')
        table.heading('product_expiration_date', text='Expiration Date')
        table.heading('description', text='Description')
        table.heading('code', text='Barcode')
        table.grid(row=1, column=0, columnspan=3, sticky='ew', padx=(25, 25), pady=(0, 25))

        productSQL = ProductSQL()
        products = productSQL.GetAll()

        for product in products:
            table.insert(parent='', index='end',
                              values=(
                                  product.id.get(),
                                  product.name.get(),
                                  product.product_expiration_date.get(),
                                  product.description.get(),
                                  product.storage_code.get()
                              ))

        table.bind("<Double-1>", self.ProductDetail) #Double mouse click func bind

    def ProductDetail(self, event):
        focus_item = event.widget.focus()
        if focus_item:
            item = event.widget.item(focus_item)
            values = item['values']
            product_id = str(values[0])
            self.main_window.show_product_detail(product_id, self)
        return
