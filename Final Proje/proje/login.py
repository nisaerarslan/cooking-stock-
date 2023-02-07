import tkinter as tk
import tkinter.messagebox as messagebox
import assets.style as style

class Login(tk.Frame):

    def __init__(self, frame_options, main_window):
        tk.Frame.__init__(self, frame_options)

        image_logo = tk.PhotoImage(file=r'./assets/logo.png')
        label_logo = tk.Label(self, image=image_logo)
        label_logo.image = image_logo
        label_logo.grid(column=0, row=0, columnspan=2, padx=(25, 10), pady=(10, 10))


        image_mesut = tk.PhotoImage(file=r'./assets/photo.png')
        label_mesut = tk.Label(self, image=image_mesut)
        label_mesut.image = image_mesut
        label_mesut.grid(column=0, row=1, rowspan=3, padx=(25, 25), pady=(25, 25))

        image_product = tk.PhotoImage(file=r"assets/menu.png")
        button_product = tk.Button(self, image=image_product, command=lambda: main_window.show_menu(self),
                                   bd=0, highlightthickness=0)
        button_product.image = image_product
        button_product.grid(column=1, row=1, padx=(0, 25), pady=(0, 0))

        image_product = tk.PhotoImage(file=r"assets/about_us.png")
        button_product = tk.Button(self, image=image_product, command=self.AboutUS,
                                   bd=0, highlightthickness=0)
        button_product.image = image_product
        button_product.grid(column=1, row=2, padx=(0, 25), pady=(0, 0))

        image_raw = tk.PhotoImage(file=r"assets/quit_app.png")
        button_raw = tk.Button(self, image=image_raw, command=quit,
                               bd=0, highlightthickness=0)
        button_raw.image = image_raw
        button_raw.grid(column=1, row=3, padx=(0, 25), pady=(0, 0))

    def AboutUS(self):
        messagebox.showinfo("Prepared By", "Ismail Deniz Coskun 200444029\nNisa Nur Erarslan 200444044\nSıla Polat 200444027\nFatih Unal 200444023")
