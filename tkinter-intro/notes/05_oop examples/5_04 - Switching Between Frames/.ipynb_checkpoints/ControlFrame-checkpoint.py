import tkinter as tk
from tkinter import ttk
from ConverterFrame import ConverterFrame
from TemperatureConverter import TemperatureConverter


class ControlFrame(tk.LabelFrame):

    def __init__(self, container):
        super().__init__(container)
        self["text"] = "Options"

        # field options
        options = {"padx": 5, "pady": 5}

        # add radio buttons

        self.selected_value = tk.IntVar()

        f_select_btn = ttk.Radiobutton(
            self,
            text="F to C",
            variable=self.selected_value,
            value=0,
            command=self.change_frame
        )
        f_select_btn.grid(column=0, row=0, **options)

        c_select_btn = ttk.Radiobutton(
            self,
            text="C to F",
            variable=self.selected_value,
            value=1,
            command=self.change_frame
        )
        c_select_btn.grid(column=1, row=0, **options)

        # add label frame to the parent window
        self.grid(column=0, row=1, sticky="ew", **options)

        # initialize the converter frames
        self.frames = {}
        self.frames[0] = ConverterFrame(container, "Fahrenheit", TemperatureConverter.f_to_c)
        self.frames[1] = ConverterFrame(container, "Celsius", TemperatureConverter.c_to_f)

        self.change_frame()

    def change_frame(self):
        frame = self.frames[self.selected_value.get()]
        frame.reset()
        frame.tkraise()
