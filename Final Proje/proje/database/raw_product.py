import tkinter as tk

from .sql import SQL


class RawProduct:
    def __init__(self, id, product_id, raw_id):
        self.RawProductSQL = RawProductSQL()
        self.id = tk.StringVar(value=id)
        self.product_id = tk.StringVar(value=product_id)
        self.raw_id = tk.StringVar(value=raw_id)

    def Add(self):
        self.RawProductSQL.Insert(
            self.product_id.get(),
            self.raw_id.get()
        )

class RawProductSQL(SQL):

    def GetAll(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM raw_product")
        temp = cursor.fetchall()
        array = []
        for raw in temp:
            array.append(RawProduct(raw[0], raw[1], raw[2]))
        return array

    def Insert(self, product_id, raw_id):
        cursor = self.connection.cursor()
        request = "INSERT INTO raw_product " \
                  "(product_id, raw_id) " \
                  "VALUES (%s, %s)"
        cursor.execute(
            request,
            (
                product_id or None,
                raw_id or None
            )
        )

    def GetSingle(self, id):
        # Won't Usage
        pass

    def Delete(self, id):
        # Won't Usage
        pass

    def Update(self):
        # Won't Usage
        pass

    def GetProductRaws(self, product_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM raw_product WHERE product_id = " + product_id)
        temp = cursor.fetchall()
        array = []
        for raw in temp:
            array.append(raw[2])
        return array

    def DeleteProductRaws(self, product_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM raw_product WHERE product_id = " + product_id)

    def GetRawProducts(self, raw_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM raw_product WHERE raw_id = " + raw_id)
        temp = cursor.fetchall()
        array = []
        for raw in temp:
            array.append(raw[1])
        return array

    def DeleteRawProducts(self, raw_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM raw_product WHERE raw_id = " + raw_id)