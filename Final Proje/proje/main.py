import tkinter as tk

from menu import Menu
from window_camera import camera
from window_product_list import WindowProductList
from window_product_add import WindowProductAdd
from window_product_detail import WindowProductDetail
from window_raw_list import WindowRawList
from window_raw_add import WindowRawAdd
from window_raw_detail import WindowRawDetail
from login import Login

'''
                                                PLEASE RUN ONLY THIS PAGE
'''


class Visualize(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.__frame_options = tk.Frame(self)
        self.__frame_options.pack(side='top', fill='both', expand=True)

        self.show_login(None)

    def show_menu(self, old_frame):
        if old_frame:
            old_frame.grid_forget()
        frame = Menu(self.__frame_options, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def show_camera(self):
        camera()

    def show_product_list(self, old_frame):
        if old_frame:
            old_frame.grid_forget()
        frame = WindowProductList(self.__frame_options, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def show_product_add(self, old_frame):
        if old_frame:
            old_frame.grid_forget()
        frame = WindowProductAdd(self.__frame_options, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def show_product_detail(self, product_id, old_frame):
        if old_frame:
            old_frame.grid_forget()
        frame = WindowProductDetail(self.__frame_options, self, product_id)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def show_raw_list(self, old_frame):
        if old_frame:
            old_frame.grid_forget()
        frame = WindowRawList(self.__frame_options, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def show_raw_add(self, old_frame):
        if old_frame:
            old_frame.grid_forget()
        frame = WindowRawAdd(self.__frame_options, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def show_raw_detail(self, raw_id, old_frame):
        if old_frame:
            old_frame.grid_forget()
        frame = WindowRawDetail(self.__frame_options, self, raw_id)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def show_login(self, old_frame):
        if old_frame:
            old_frame.grid_forget()
        frame = Login(self.__frame_options, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

window = Visualize()
window.resizable(width=False, height=False)
window.title("Cooking School - Stock Program")
window.mainloop()
