import tkinter.messagebox as messagebox
import tkinter as tk

from .sql import SQL


class RawMaterials():
    def __init__(self, id, name, dop, nos, sed, sc, desc, img=None):
        self.rawSQL = RawSQL()
        self.id = tk.StringVar(value=id)
        self.name = tk.StringVar(value=name)
        self.date_of_purchase = tk.StringVar(value=dop)
        self.name_of_supplier = tk.StringVar(value=nos)
        self.storage_expiration_date = tk.StringVar(value=sed)
        self.storage_code = tk.StringVar(value=sc)
        self.description = tk.StringVar(value=desc)
        self.image = img

    def Add(self):
        return self.rawSQL.Insert(
            self.name.get(),
            self.date_of_purchase.get(),
            self.name_of_supplier.get(),
            self.storage_expiration_date.get(),
            self.storage_code.get(),
            self.description.get(),
            self.image
        )

    def Update(self):
        self.rawSQL.Update(
            self.id.get(),
            self.name.get(),
            self.date_of_purchase.get(),
            self.name_of_supplier.get(),
            self.storage_expiration_date.get(),
            self.storage_code.get(),
            self.description.get(),
            self.image
        )

    def Delete(self):
        self.rawSQL.Delete(self.id.get())

class RawSQL(SQL):

    def GetAll(self): #overrided abstract function
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM raw")
        temp = cursor.fetchall()
        array = [] # For abstracting data from database
        for raw in temp:
            array.append(RawMaterials(raw[0], raw[1], raw[2], raw[3], raw[4], raw[5], raw[6], raw[7]))
        return array

    def GetSingle(self, raw_id): #overrided abstract function
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM raw WHERE id = " + str(raw_id)) #Get the id of the data from the database
        temp = cursor.fetchone()
        return RawMaterials(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7])

    def Delete(self, raw_id): #overrided abstract function
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM raw WHERE id = " + str(raw_id)) #Get the id of the data from the database
        messagebox.showinfo('Success!', 'Material deleted successfully.')

    def Update(self, raw_id, name, dop, nos, sed, sc, desc, img): #overrided abstract function
        cursor = self.connection.cursor() #%s is used to simplify sql queries
        request = "UPDATE raw SET " \
                  "name = %s, " \
                  "date_of_purchase = %s, " \
                  "name_of_supplier = %s, "\
                  "storage_expiration_date = %s, "\
                  "storage_code = %s, "\
                  "description = %s, "\
                  "image = %s "\
                  "WHERE id = %s"
        cursor.execute(
            request,
            (
                name or None,
                dop or None,
                nos or None,
                sed or None,
                sc or None,
                desc or None,
                img or None,
                raw_id
            )
        )
        messagebox.showinfo('Success!', 'Material updated successfully.')

    def Insert(self, name, dop, nos, sed, sc, desc, img): #overrided abstract function
        cursor = self.connection.cursor()
        request = "INSERT INTO raw " \
                  "(name, date_of_purchase, name_of_supplier, storage_expiration_date, storage_code, description, image) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s)" #%s is used to simplify sql queries
        cursor.execute(
            request,
            (
                name or None,
                dop or None,
                nos or None,
                sed or None,
                sc or None,
                desc or None,
                img or None
            )
        )
        messagebox.showinfo('Success!', 'Material added successfully.')
        return cursor.lastrowid