import tkinter as tk
from tkinter import ttk


class Mile_To_Km_Converter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mile to Km Converter")
        self.attributes("-topmost", 1)
        self.config(padx=20, pady=20)

        self.miles = tk.StringVar()
        self.entry = ttk.Entry(self, textvariable=self.miles, width=6)
        self.entry.grid(column=1, row=0)

        self.label_miles = ttk.Label(self, text='Miles')
        self.label_miles.grid(column=2, row=0)

        self.label_message = ttk.Label(self, text='is equal to')
        self.label_message.grid(column=0, row=1)

        self.label_result = ttk.Label(self, text='')
        self.label_result.grid(column=1, row=1)

        self.label_km = ttk.Label(self, text='Km')
        self.label_km.grid(column=2, row=1)

        self.btn_convert = ttk.Button(self, text='Calculate', command=self.btn_convert_clicked)
        self.btn_convert.grid(column=1, row=2)

    def btn_convert_clicked(self):
        result = float(self.miles.get()) * 1.609
        self.label_result.config(text=f"{result}")


if __name__ == "__main__":
    app = Mile_To_Km_Converter()
    app.mainloop()
