import base64
import tkinter as tk
import assets.style as style

from database.product import ProductSQL
from database.raw import RawSQL
from database.raw_product import RawProductSQL
from tkinter import filedialog

class WindowProductDetail(tk.Frame):

    def __init__(self, frame_options, main_window, product_id):
        tk.Frame.__init__(self, frame_options)
        self.main_window = main_window

        tk.Button(self, text='📄 Back To List', command=lambda: main_window.show_product_list(self)) \
            .grid(column=0, row=0, sticky='ew', padx=(25, 25), pady=(25, 25))
        tk.Label(self, text='CSSP - Food Detail', font=style.title_font).grid(column=1, row=0, padx=(0, 25))

        productSQL = ProductSQL()
        self.product = productSQL.GetSingle(product_id)

        rawSQL = RawSQL()
        self.raws = rawSQL.GetAll()

        tk.Label(self, text="Name").grid(row=1, sticky='w', padx=(25, 0), pady=(0, 5))
        tk.Entry(self, textvariable=self.product.name).grid(row=1, column=1, padx=(0, 25), sticky='ew')

        tk.Label(self, text="Date of Production").grid(row=2, sticky='w', padx=(25, 0), pady=(5, 5))
        tk.Entry(self, textvariable=self.product.date_of_production).grid(row=2, column=1, padx=(0, 25), sticky='ew')

        tk.Label(self, text="Name of Customer").grid(row=3, sticky='w', padx=(25, 0), pady=(5, 5))
        tk.Entry(self, textvariable=self.product.name_of_customer).grid(row=3, column=1, padx=(0, 25), sticky='ew')

        tk.Label(self, text="Product Expiration Date").grid(row=4, sticky='w', padx=(25, 0), pady=(5, 5))
        tk.Entry(self, textvariable=self.product.product_expiration_date).grid(row=4, column=1, padx=(0, 25), sticky='ew')

        tk.Label(self, text="Storage Code").grid(row=5, sticky='w', padx=(25, 0), pady=(5, 5))
        tk.Entry(self, textvariable=self.product.storage_code).grid(row=5, column=1, padx=(0, 25), sticky='ew')

        tk.Label(self, text="Description").grid(row=6, sticky='w', padx=(25, 0), pady=(5, 5))
        tk.Entry(self, textvariable=self.product.description).grid(row=6, column=1, padx=(0, 25), sticky='ew')

        rawSQL = RawSQL()
        raws = rawSQL.GetAll()
        rawProductSQL = RawProductSQL()
        selected_raws = rawProductSQL.GetProductRaws(product_id)
        mb = tk.Menubutton(self, text="👇🏻 Select Raws From List", relief=tk.RAISED)
        mb.menu = tk.Menu(mb, tearoff=0)
        mb["menu"] = mb.menu
        self.menu_raws = {}
        for raw in raws:
            if int(raw.id.get()) in selected_raws:
                default_value = 1
            else:
                default_value = 0
            var = tk.IntVar(value=default_value)
            mb.menu.add_checkbutton(label=raw.name.get(), variable=var, onvalue=1, offvalue=0)
            self.menu_raws[raw.id.get()] = var
        mb.grid(row=7, columnspan=2, sticky='ew', padx=(25, 25), pady=(5, 0))

        tk.Button(self, text="🌇 Take Image", command=lambda: self.UploadFile()) \
            .grid(row=8, sticky='ew', padx=(25, 5), pady=(5, 5))
        tk.Button(self, text="🗑️ Delete Image", command=self.DeleteFile) \
            .grid(row=8, column=1, sticky='ew', padx=(5, 25), pady=(5, 5))
        if self.product.image:
            stock_image = tk.PhotoImage(data=base64.b64decode(self.product.image))
            self.product_image = tk.Label(self, image=stock_image)
            self.product_image.image = stock_image
            self.product_image.grid(row=9, columnspan=2, padx=(25, 25), pady=(5, 5))
        else:
            self.product_image = tk.Label(self)

        tk.Button(self, text="✔️ Update", command=self.UpdateProduct) \
            .grid(row=10, columnspan=2, sticky='ew', padx=(25, 25), pady=(0, 5))
        tk.Button(self, text="❌ Delete", command=self.DeleteProduct) \
            .grid(row=11, columnspan=2, sticky='ew', padx=(25, 25), pady=(0, 25))

    def UploadFile(self):#This function allows to change the picture of the new or old added product.
        filename = filedialog.askopenfilename(filetypes=[('Png Files', '*.png')])
        if filename:
            img = tk.PhotoImage(file=filename)

            if self.product_image:
                self.product_image.destroy()
            self.product_image = tk.Label(self, image=img)
            self.product_image.image = img
            self.product_image.grid(row=9, columnspan=2, padx=(25, 25), pady=(5, 5))

            self.product.image = base64.b64encode(open(filename, 'rb').read())

    def DeleteFile(self):#deletes the uploaded image
        if self.product_image:
            self.product_image.destroy()
        self.product.image = None

    def UpdateProduct(self):#Allows us to save changes to the product
        self.product.Update()
        rawProductSQL = RawProductSQL()
        rawProductSQL.DeleteProductRaws(self.product.id.get())
        for raw_id in self.menu_raws:
            if self.menu_raws[raw_id].get() == 1:
                rawProductSQL.Insert(self.product.id.get(), raw_id)
        self.main_window.show_product_list(self)

    def DeleteProduct(self):
        rawProductSQL = RawProductSQL()
        rawProductSQL.DeleteProductRaws(self.product.id.get())
        #Before product is deleted, the raw_product table row's it depends on must be deleted.
        #If raw_prodcut table row's are not deleted, product will get foreign key error while deleting.
        self.product.Delete()
        self.main_window.show_product_list(self)
