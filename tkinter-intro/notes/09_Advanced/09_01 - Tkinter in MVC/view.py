from tkinter import ttk
import tkinter as tk


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(self, text='Email:')
        self.label.grid(row=0, column=0)

        # email entry
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=0, column=1, sticky=tk.NSEW)

        # save button
        self.save_btn = ttk.Button(self, text='Save', command=self.save_btn_clicked)
        self.save_btn.grid(row=0, column=2, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=1, column=1, sticky=tk.W)

        # set the controller
        self.controller = None

    def save_btn_clicked(self):
        if self.controller:
            self.controller.save(self.email_var.get())

    def set_controller(self, controller):
        self.controller = controller

    def show_error(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)

        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        self.message_label.config(text=message, foreground='green')
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        self.message_label.config(text='')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('test')
    view = View(root)
    view.grid(row=0, column=0, padx=10, pady=10)
    root.mainloop()
