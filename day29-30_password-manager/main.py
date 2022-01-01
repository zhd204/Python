import json
import tkinter as tk
from tkinter import messagebox
import random
import pyperclip


class Pwd_Mgr(tk.Tk):
    # ---------------------------- UI SETUP ------------------------------- #
    def __init__(self):
        super().__init__()

        self.title("Password Manager")
        self.attributes("-topmost", 1)
        self.config(padx=50, pady=50)

        # logo
        self.canvas = tk.Canvas(self, width=200, height=200)
        self.canvas_image = tk.PhotoImage(file="logo.png")
        self.canvas.create_image(110, 110, image=self.canvas_image)
        self.canvas.grid(row=0, column=1)

        # label - website
        self.lbl_website = tk.Label(self, text="Website:")
        self.lbl_website.grid(row=1, column=0)

        # label - email/username
        self.lbl_username = tk.Label(self, text="Email/Username:")
        self.lbl_username.grid(row=2, column=0)

        # label - password
        self.lbl_password = tk.Label(self, text="Password:")
        self.lbl_password.grid(row=3, column=0)

        # entry - website
        self.entry_website_text = tk.StringVar()
        self.entry_website = tk.Entry(self, textvariable=self.entry_website_text, width=21)
        self.entry_website.grid(row=1, column=1)
        self.entry_website.focus()

        # entry - email/username
        self.entry_username_text = tk.StringVar()
        self.entry_username = tk.Entry(self, textvariable=self.entry_username_text, width=35)
        self.entry_username.grid(row=2, column=1, columnspan=2)
        self.entry_username.insert(tk.END, "unknown@gmail.com")

        # entry - password
        self.entry_password_text = tk.StringVar()
        self.entry_password = tk.Entry(self, textvariable=self.entry_password_text, width=21, show="*")
        self.entry_password.grid(row=3, column=1)

        # button - search
        self.btn_search = tk.Button(self, text="Search", command=self.search, width=14)
        self.btn_search.grid(row=1, column=2)

        # button - generate password
        self.btn_gen_pwd = tk.Button(self, text="Generate Password", command=self.pwd_gen)
        self.btn_gen_pwd.grid(row=3, column=2)

        # button - add
        self.btn_add = tk.Button(self, text="Add", width=36, command=self.save)
        self.btn_add.grid(row=4, column=1, columnspan=2)

    # ---------------------------- PASSWORD GENERATOR --------------------- #
    def pwd_gen(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_numbers = random.randint(2, 4)
        nr_symbols = random.randint(2, 4)

        password_list = []

        password_list.extend([random.choice(letters) for _ in range(nr_letters)])
        password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])
        password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])

        random.shuffle(password_list)

        password = "".join(password_list)

        self.entry_password_text.set(password)
        pyperclip.copy(password)

    # ---------------------------- SAVE PASSWORD -------------------------- #
    def save(self):

        website = self.entry_website_text.get()
        username = self.entry_username_text.get()  # use email as the username
        password = self.entry_password_text.get()

        # info = website + " | " + username + " | " + password

        new_data = {
            website: {
                "email": username,
                "password": password
            }
        }

        if all((len(website), len(username), len(password))):

            if self.msg_confirm():

                # with open("user_info.txt", "a") as f:
                #     f.write(info)
                #     f.write("\n")
                #
                # self.entry_website_text.set("")
                # # self.entry_username_text.set("")
                # self.entry_password_text.set("")
                try:
                    with open("data.json", "r") as data_file:
                        # reading old data
                        data = json.load(data_file)
                except FileNotFoundError:
                    with open("data.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                    # updating old data with the new data
                    data.update(new_data)

                    with open("data.json", "w") as data_file:
                        # saving updated data
                        json.dump(data, data_file, indent=4)
                finally:
                    self.entry_website_text.set("")
                    # self.entry_username_text.set("")
                    self.entry_password_text.set("")

                self.msg_info1()
            else:
                self.msg_info2()
        else:
            messagebox.showwarning(title="Warning", message="Please fill in any blanks.")

    # ---------------------------- MESSAGE DIALOGS -------------------------- #
    @staticmethod
    def msg_confirm():
        answer = messagebox.askyesno(title="Confirmation", message="Are you sure that you want to add this credential?")

        return answer

    @staticmethod
    def msg_info1():
        messagebox.showinfo(title="Information", message="The credential has been added.")

    @staticmethod
    def msg_info2():
        messagebox.showinfo(title="Information", message="The credential has NOT been added.")

    # ---------------------------- Profile Search --------------------- #
    def search(self):
        website = self.entry_website_text.get()

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showwarning(title="Warning", message="No Data File Found.")
            return
        else:
            try:
                profile_dict = data[website]
            except KeyError:
                messagebox.showwarning(title="Warning",
                                       message="No details for the website exists.")
                return
            else:
                email = profile_dict["email"]
                password = profile_dict["password"]
                messagebox.showinfo(title="Information", message=f"Email:{email}\nPassword:{password}.")


if __name__ == "__main__":
    app = Pwd_Mgr()
    app.mainloop()
