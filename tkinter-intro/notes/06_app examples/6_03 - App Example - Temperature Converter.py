import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# root window
root = tk.Tk()
root.geometry("400x75")
root.title("Temperature Converter")
root.attributes("-topmost", 1)


# button event handler
def convert_btn_clicked():
    try:
        temp_f_float = float(temp_f.get())
        temp_c_float = (temp_f_float - 32) / 1.8
        result_lbl.config(text=f"{temp_f_float:.2f} Fahrenheit = {temp_c_float:.2f} Celsius")
    except ValueError as error:
        messagebox.showerror(title="Error", message=error)


# main frame for conversion from F to C
frame1 = ttk.Frame(root)
frame1.grid(column=0, row=0, padx=10, pady=10)

# field options
options = {'padx': 5, 'pady': 5}

# frame1.columnconfigure(0, weight=1)
# frame1.columnconfigure(1, weight=1)
# frame1.columnconfigure(2, weight=1)

# temperature label for Fahrenheit
temp_label = ttk.Label(frame1, text="Fahrenheit")
temp_label.grid(column=0, row=0, sticky=tk.W, **options)

# temperature entry field for Fahrenheit
temp_f = tk.StringVar()
temp_f_entry = ttk.Entry(frame1, textvariable=temp_f)
temp_f_entry.grid(column=1, row=0, **options)
temp_f_entry.focus()

result_lbl = ttk.Label(frame1)
result_lbl.grid(columnspan=3, row=1, **options)

convert_btn = ttk.Button(frame1, text="Convert", command=convert_btn_clicked)
convert_btn.grid(column=2, row=0, sticky=tk.E, **options)

root.mainloop()
