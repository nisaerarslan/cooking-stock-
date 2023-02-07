import tkinter as tk
import assets.style as style

class Menu(tk.Frame):

    def __init__(self, frame_options, main_window):
        tk.Frame.__init__(self, frame_options)

        tk.Label(self, text='CSSP - Menu', font=style.title_font).grid(column=0, row=0, padx=(25, 25), pady=(25, 25))

        image_product = tk.PhotoImage(file=r"./assets/button_food.png")
        button_product = tk.Button(self, image=image_product, command=lambda: main_window.show_product_list(self),
                                   bd=0, highlightthickness=0)
        button_product.image = image_product
        button_product.grid(column=0, row=1, padx=(25, 25), pady=(0, 10))

        image_raw = tk.PhotoImage(file=r"./assets/button_material.png")
        button_raw = tk.Button(self, image=image_raw, command=lambda: main_window.show_raw_list(self),
                               bd=0, highlightthickness=0)
        button_raw.image = image_raw
        button_raw.grid(column=0, row=2, padx=(25, 25), pady=(0, 25))

        image_camera = tk.PhotoImage(file=r"./assets/button_camera.png")
        button_camera = tk.Button(self, image=image_camera, command=lambda: main_window.show_camera(),
                                  bd=0, highlightthickness=0)
        button_camera.image = image_camera
        button_camera.grid(column=0, row=3, padx=(25, 25), pady=(25, 25))
