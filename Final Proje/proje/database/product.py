import tkinter.messagebox as messagebox
import tkinter as tk

from .sql import SQL
from .raw import RawMaterials


class Product(RawMaterials): #Product inherit raw materials
    def __init__(self, id, name, dop, noc, ped, sc, desc, img):
        super().__init__(id, name, dop, noc, ped, sc, desc, img)
        self.productSQL = ProductSQL()
        self.date_of_production = tk.StringVar(value=dop)
        self.name_of_customer = tk.StringVar(value=noc)
        self.product_expiration_date = tk.StringVar(value=ped)

    def Add(self): #overrided function
        return self.productSQL.Insert(
            self.name.get(),
            self.date_of_production.get(),
            self.name_of_customer.get(),
            self.product_expiration_date.get(),
            self.storage_code.get(),
            self.description.get(),
            self.image
        )

    def Update(self): #overrided function
        self.productSQL.Update(
            self.id.get(),
            self.name.get(),
            self.date_of_production.get(),
            self.name_of_customer.get(),
            self.product_expiration_date.get(),
            self.storage_code.get(),
            self.description.get(),
            self.image
        )

    def Delete(self): #overrided function
        self.productSQL.Delete(self.id.get())


class ProductSQL(SQL):

    def GetAll(self): #overrided abstract function
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM product")
        temp = cursor.fetchall()
        array = []
        for product in temp:
            array.append(
                Product(product[0], product[1], product[3], product[2], product[4], product[5], product[6], product[7]))
        return array

    def GetSingle(self, product_id): #overrided abstract function
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM product WHERE id = " + str(product_id))
        temp = cursor.fetchone()
        return Product(temp[0], temp[1], temp[3], temp[2], temp[4], temp[5], temp[6], temp[7])

    def Delete(self, product_id): #overrided abstract function
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM product WHERE id = " + str(product_id))
        messagebox.showinfo('Success!', 'Food deleted successfully.')

    def Update(self, product_id, name, dop, noc, ped, sc, desc, img): #overrided abstract function
        cursor = self.connection.cursor()
        request = "UPDATE product SET " \
                  "name = %s, " \
                  "date_of_production = %s, " \
                  "name_of_customer = %s, " \
                  "product_expiration_date = %s, " \
                  "storage_code = %s, " \
                  "description = %s, " \
                  "image = %s " \
                  "WHERE id = %s"
        cursor.execute(
            request,
            (
                name or None,
                dop or None,
                noc or None,
                ped or None,
                sc or None,
                desc or None,
                img or None,
                product_id
            )
        )
        messagebox.showinfo('Success!', 'Food updated successfully.')

    def Insert(self, name, dop, noc, ped, sc, desc, img): #overrided abstract function
        cursor = self.connection.cursor()
        request = "INSERT INTO product " \
                  "(name, date_of_production, name_of_customer, product_expiration_date, storage_code, description, image) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(
            request,
            (
                name or None,
                dop or None,
                noc or None,
                ped or None,
                sc or None,
                desc or None,
                img or None
            )
        )
        messagebox.showinfo('Success!', 'Food added successfully.')
        return cursor.lastrowid
