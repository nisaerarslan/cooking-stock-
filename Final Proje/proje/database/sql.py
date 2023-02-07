import mysql.connector
from abc import ABC, abstractmethod


class SQL(ABC):

    def __init__(self): #Please change sql settings here
        self.connection = mysql.connector.connect(
            host='localhost',
            port='3307',
            user='root',
            password='',
            database='proje',
            autocommit=True
        )

    @abstractmethod
    def GetAll(self):
        pass

    @abstractmethod
    def GetSingle(self, id):
        pass

    @abstractmethod
    def Delete(self, id):
        pass

    @abstractmethod
    def Insert(self, *args, **kwargs):
        pass

    @abstractmethod
    def Update(self, *args, **kwargs):
        pass