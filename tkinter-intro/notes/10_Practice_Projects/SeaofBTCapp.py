# https://github.com/Sea-of-BTC/Bitcoin-Trading-Client
# https://pythonprogramming.net/tkinter-depth-tutorial-making-actual-program/

import tkinter as tk
from tkinter import ttk

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import urllib
import json

import pandas as pd
import numpy as np

LARGE_FONT = ("Verdana", 16)
style.use("ggplot")

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)


def animate(i):
    with open("sampletext.txt", "r") as file:
        pull_data = file.read()
        data_list = pull_data.split('\n')
        x_list = []
        y_list = []
        for line in data_list:
            if len(line) > 1:
                x, y = line.split(",")
                x_list.append(x)
                y_list.append(y)
    a.clear()
    a.plot(x_list, y_list)


class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.iconbitmap("clienticon.ico")  # for windows
        self.title("Sea of BTC Client")
        self.attributes("-topmost", 1)

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, BTCe_Page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ttk.Label(self, text="""        Bitcoin trading application.
        Use at your own risk.
        There is no warranty.""", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        button1 = ttk.Button(self, text="Agree",
                             command=lambda: controller.show_frame(BTCe_Page))
        button1.pack()

        button2 = ttk.Button(self, text="Disagree",
                             command=quit)
        button2.pack()

        # button3 = ttk.Button(self, text="Graph Page",
        #                      command=lambda: controller.show_frame(PageThree))
        # button3.pack()


class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ttk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        button = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()

        # button2 = ttk.Button(self, text="Visit Page 2",
        #                      command=lambda: controller.show_frame(PageTwo))
        # button2.pack()


class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ttk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        button = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()

        button1 = ttk.Button(self, text="Visit Page 1",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()


class BTCe_Page(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ttk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        button = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()


app = SeaofBTCapp()
ani = animation.FuncAnimation(f, animate, interval=100)
app.mainloop()
