import tkinter as tk
from tkinter import messagebox

import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"


class Flashcard(tk.Tk):

    def __init__(self):
        super().__init__()

        # convert pandas data frame to dictionary
        try:
            self.df_word = pd.read_csv("data/french_words_to_learn.csv")
        except FileNotFoundError:
            self.df_word = pd.read_csv("data/french_words.csv")

        # self.dict_word = self.df_word.to_dict('records')
        self.dict_word = self.df_word.to_dict()
        # construct French-English dictionary
        self.french_word_pool = [{self.dict_word["French"][i]: self.dict_word["English"][i]} for i in
                                 range(len(self.dict_word["French"]))]

        self.title("Flashy")
        self.attributes("-topmost", 1)
        self.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
        self.current_card = None

        # canvas - image
        self.card_front_img = tk.PhotoImage(file="images/card_front.png")
        self.card_back_img = tk.PhotoImage(file="images/card_back.png")
        self.canvas = tk.Canvas(self, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas_image = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.canvas.grid(row=0, column=0, columnspan=2)

        # canvas - title text
        # self.title_text = tk.StringVar()
        self.canvas_title_text = self.canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))

        # canvas - title text
        # self.word_text = tk.StringVar()
        self.canvas_word_text = self.canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))

        # wrong button
        self.wrong_img = tk.PhotoImage(file="images/wrong.png")
        self.wrong_button = tk.Button(self, width=100, height=99, image=self.wrong_img,
                                      highlightthickness=0, command=self.next_card_cross)
        self.wrong_button.grid(row=1, column=0)

        # right button
        self.right_img = tk.PhotoImage(file="images/right.png")
        self.right_button = tk.Button(self, width=100, height=99, image=self.right_img,
                                      highlightthickness=0, command=self.next_card_check)
        self.right_button.grid(row=1, column=1)

        self.timer = self.after(3000, lambda: self.flip_card())
        self.next_card_cross()

    def next_card_check(self):
        self.after_cancel(self.timer)
        self.update_word_pool()
        self.gen_word()
        self.canvas.itemconfig(self.canvas_image, image=self.card_front_img)
        self.canvas.itemconfig(self.canvas_title_text, text="French", fill="black")
        self.canvas.itemconfig(self.canvas_word_text, text=self.current_card[0], fill="black")

        self.timer = self.after(3000, lambda: self.flip_card())

    def next_card_cross(self):
        self.after_cancel(self.timer)
        self.gen_word()
        self.canvas.itemconfig(self.canvas_image, image=self.card_front_img)
        self.canvas.itemconfig(self.canvas_title_text, text="French", fill="black")
        self.canvas.itemconfig(self.canvas_word_text, text=self.current_card[0], fill="black")

        self.timer = self.after(3000, lambda: self.flip_card())

    def flip_card(self):
        self.canvas.itemconfig(self.canvas_image, image=self.card_back_img)
        self.canvas.itemconfig(self.canvas_title_text, text="English", fill="white")
        self.canvas.itemconfig(self.canvas_word_text, text=self.current_card[1], fill="white")

    def gen_word(self):

        random_word_pair = tuple(*random.choice(self.french_word_pool).items())

        self.current_card = random_word_pair

    def update_word_pool(self):
        self.french_word_pool.remove({self.current_card[0]: self.current_card[1]})
        # convert the list of dictionaries to the list of lists
        updated_word_pool_ls = [list(*self.french_word_pool[i].items()) for i in range(len(self.french_word_pool))]
        # create updated dataframe
        updated_word_pool_df = pd.DataFrame(updated_word_pool_ls, columns=['French', 'English'])
        # create updated csv file
        updated_word_pool_df.to_csv("data/french_words_to_learn.csv", index=False)


if __name__ == "__main__":
    app = Flashcard()
    app.mainloop()
