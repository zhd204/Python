import math
import tkinter as tk
from tkinter import ttk
import datetime

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None


class Pomodoro(tk.Tk):
    # ---------------------------- UI SETUP ------------------------------- #
    def __init__(self):
        super().__init__()
        self.marks = ""
        self.title("Pomodoro")
        self.config(padx=100, pady=100, bg=YELLOW)

        # tomato image
        self.canvas = tk.Canvas(self, width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.tomato_img = tk.PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.canvas.grid(column=1, row=1)

        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

        # timer label
        self.lbl_timer = tk.Label(self, bg=YELLOW, fg=GREEN, text="Timer", font=(FONT_NAME, 40))
        self.lbl_timer.grid(column=1, row=0)

        # start button
        self.btn_start = tk.Button(self, text="Start", highlightthickness=0, command=lambda: self.start_timer())
        self.btn_start.grid(column=0, row=2)

        # reset button
        self.btn_reset = tk.Button(self, text="Reset", highlightthickness=0, command=lambda: self.reset_timer())
        self.btn_reset.grid(column=2, row=2)

        # check mark label
        self.lbl_checkmark_text = tk.StringVar()
        self.lbl_checkmark = tk.Label(self, textvariable=self.lbl_checkmark_text, fg=GREEN, bg=YELLOW)
        self.lbl_checkmark.grid(column=1, row=3)

    # ---------------------------- TIMER RESET ------------------------------- #
    def reset_timer(self):
        global reps
        reps = 0
        self.after_cancel(timer)
        self.lbl_timer.config(text="Timer", fg=GREEN)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.marks = ""
        self.btn_start.config(state=tk.NORMAL)

    # ---------------------------- TIMER MECHANISM ------------------------------- #
    def start_timer(self):
        global reps
        reps += 1

        self.btn_start.config(state=tk.DISABLED)
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            self.count_down(long_break_sec)
            self.lbl_timer.config(text="Break", fg=RED)
        elif reps % 2 == 0:
            self.count_down(short_break_sec)
            self.lbl_timer.config(text="Break", fg=PINK)
        else:
            self.count_down(work_sec)
            self.lbl_timer.config(text=" Work ", fg=GREEN)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
    def count_down(self, count_in_sec):
        global reps
        global timer
        converted_time = self.convert(count_in_sec)
        self.canvas.itemconfig(self.timer_text, text=converted_time)
        if count_in_sec > 0:
            timer = self.after(1000, self.count_down, count_in_sec - 1)
        else:
            for _ in range(math.floor(reps / 2)):
                self.marks += "✔"
            self.lbl_checkmark_text.set(self.marks)
            self.start_timer()

    # convert seconds into hours, minutes and seconds
    @staticmethod
    def convert(n):
        reference = datetime.datetime(1900, 1, 1, 0, 0, 0, 0)
        t = reference + datetime.timedelta(seconds=n)
        return t.strftime("%M:%S")


if __name__ == "__main__":
    app = Pomodoro()
    app.mainloop()
