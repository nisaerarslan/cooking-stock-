import tkinter as tk
import base64
import assets.style as style

from database.raw import RawMaterials
from database.product import ProductSQL
from database.raw_product import RawProductSQL
from tkinter import filedialog

class WindowRawAdd(tk.Frame):

    def __init__(self, frame_options, main_window):
        tk.Frame.__init__(self, frame_options)
        self.main_window = main_window

        tk.Button(self, text='📄 Back To List', command=lambda: main_window.show_raw_list(self)) \
            .grid(column=0, row=0, sticky='ew', padx=(25, 25), pady=(25, 25))
        tk.Label(self, text='CSSP - Material Add', font=style.title_font).grid(column=1, row=0, padx=(0, 25))

        self.raw = RawMaterials(None, '', '', '', '', '', '', '')

        tk.Label(self, text="Name").grid(row=1, sticky='w', padx=(25, 0), pady=(0, 5))
        tk.Entry(self, textvariable=self.raw.name).grid(row=1, column=1, padx=(0, 25), sticky='ew')

        tk.Label(self, text="Date of Purchase").grid(row=2, sticky='w', padx=(25, 0), pady=(5, 5))
        tk.Entry(self, textvariable=self.raw.date_of_purchase).grid(row=2, column=1, padx=(0, 25), sticky='ew')

        tk.Label(self, text="Name of Supplier").grid(row=3, sticky='w', padx=(25, 0), pady=(5, 5))
        tk.Entry(self, textvariable=self.raw.name_of_supplier).grid(row=3, column=1, padx=(0, 25), sticky='ew')

        tk.Label(self, text="Storage Expiration Date").grid(row=4, sticky='w', padx=(25, 0), pady=(5, 5))
        tk.Entry(self, textvariable=self.raw.storage_expiration_date).grid(row=4, column=1, padx=(0, 25), sticky='ew')

        tk.Label(self, text="Storage Code").grid(row=5, sticky='w', padx=(25, 0), pady=(5, 5))
        tk.Entry(self, textvariable=self.raw.storage_code).grid(row=5, column=1, padx=(0, 25), sticky='ew')

        tk.Label(self, text="Description").grid(row=6, sticky='w', padx=(25, 0), pady=(5, 5))
        tk.Entry(self, textvariable=self.raw.description).grid(row=6, column=1, padx=(0, 25), sticky='ew')

        productSQL = ProductSQL() #this field is made for data association with foreign key
        products = productSQL.GetAll()
        mb = tk.Menubutton(self, text="👇🏻 Select Foods From List", relief=tk.RAISED)
        mb.menu = tk.Menu(mb, tearoff=0)
        mb["menu"] = mb.menu
        self.menu_products = {}
        for product in products:
            var = tk.IntVar(value=0)
            mb.menu.add_checkbutton(label=product.name.get(), variable=var, onvalue=1, offvalue=0)
            self.menu_products[product.id.get()] = var
        mb.grid(row=7, columnspan=2, sticky='ew', padx=(25, 25), pady=(5, 0))

        tk.Button(self, text="🌇 Take Image", command=lambda: self.UploadFile())\
            .grid(row=8, sticky='ew', padx=(25, 5), pady=(5, 5))
        tk.Button(self, text="🗑️ Delete Image", command=self.DeleteFile)\
            .grid(row=8, column=1, sticky='ew', padx=(5, 25), pady=(5, 5))
        self.raw_image = tk.Label(self)

        tk.Button(self, text="✅ Submit", command=self.AddRaw) \
            .grid(row=10, columnspan=2, sticky='ew', padx=(25, 25), pady=(0, 25))

    def UploadFile(self): #
        filename = filedialog.askopenfilename(filetypes=[('Png Files', '*.png')])
        if filename:
            img = tk.PhotoImage(file=filename)

            if self.raw_image:
                self.raw_image.destroy()
            self.raw_image = tk.Label(self, image=img)
            self.raw_image.image = img
            self.raw_image.grid(row=9, columnspan=2, padx=(25, 25), pady=(5, 5))

            self.raw.image = base64.b64encode(open(filename, 'rb').read()) #for saving the image to the database. type conversion is required.
    def DeleteFile(self):
        if self.raw_image:
            self.raw_image.destroy()
        self.raw.image = None

    def AddRaw(self): #the code allows us to see n pieces of data so that it is extensible
        raw_id = self.raw.Add()
        if raw_id:
            rawProductSQL = RawProductSQL()
            for product_id in self.menu_products:
                if self.menu_products[product_id].get() == 1:
                    rawProductSQL.Insert(product_id, raw_id)
            self.main_window.show_raw_list(self)
