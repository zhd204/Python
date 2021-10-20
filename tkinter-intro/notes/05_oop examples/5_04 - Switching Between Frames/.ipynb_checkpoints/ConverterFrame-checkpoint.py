import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


class ConverterFrame(tk.Frame):
    def __init__(self, container, unit_from, converter):
        super().__init__(container)

        self.unit_from = unit_from
        self.converter = converter

        # field options
        options = {'padx': 5, 'pady': 5}

        # label
        self.temp_lbl = ttk.Label(self, text=self.unit_from)
        self.temp_lbl.grid(column=0, row=0, sticky=tk.W, **options)

        # entry
        self.temp = tk.StringVar()
        self.temp_entry = ttk.Entry(self, textvariable=self.temp)
        self.temp_entry.grid(column=1, row=0, **options)
        self.temp_entry.focus()

        # button
        self.convert_btn = ttk.Button(self, text="Convert", command=self.convert)
        self.convert_btn.grid(column=2, row=0, sticky=tk.W, **options)

        # result label
        self.result_lbl = ttk.Label(self)
        self.result_lbl.grid(columnspan=3, row=1, **options)

        # add frame to the parent window
        self.grid(column=0, row=0, sticky='nsew', **options)

    def convert(self):
        try:
            temp_float = float(self.temp.get())
            result = self.converter(temp_float)
            self.result_lbl.config(text=result)
        except ValueError as error:
            showerror(title="Error", message=error)

    def reset(self):
        self.temp_entry.delete(0, "end")
        self.result_lbl.text = ""
