import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")
        self.attributes("-topmost", 1)
        self.title("OOP Example - Temperature Converter")
        self.resizable(False, False)
