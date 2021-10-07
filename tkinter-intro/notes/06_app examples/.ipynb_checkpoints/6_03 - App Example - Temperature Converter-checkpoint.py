import tkinter as tk
from tkinter import ttk

root = tk.Tk()
# root.geometry("300x150")
root.title("Temperature Converter")
root.attributes("-topmost", 1)


def convert_F_to_C():
    pass


frame1 = ttk.Frame(root)
frame1.grid(column=0, row=0)


# frame1.columnconfigure(0, weight=1)
# frame1.columnconfigure(1, weight=1)
# frame1.columnconfigure(2, weight=1)

ttk.Label(frame1, text="Fahrenheit").grid(column=0, row=0)

temp_f = tk.StringVar()
temp_f_entry = ttk.Entry(frame1, textvariable=temp_f).grid(column=1, row=0, padx=5, pady=5)

convert_btn = ttk.Button(frame1, text="Convert").grid(column=2, row=0)


result = ttk.Label(frame1, text="test").grid(column=1, row=1)


root.mainloop()
