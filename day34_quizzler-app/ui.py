from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.attributes("-topmost", 1)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_text = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        image_true = PhotoImage(file="images/true.png")
        self.btn_true = Button(image=image_true, highlightthickness=0, command=lambda: self.check("True"))
        self.btn_true.grid(row=2, column=0)

        image_false = PhotoImage(file="images/false.png")
        self.btn_false = Button(image=image_false, highlightthickness=0, command=lambda: self.check("False"))
        self.btn_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def check(self, user_answer: bool):
        result = self.quiz.check_answer(user_answer)
        self.give_feedback(result)
        self.score_text.config(text=self.quiz.update_score())

    def give_feedback(self, result: bool):
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, lambda: self.canvas.config(bg="white"))
        self.window.after(1000, lambda: self.check_for_next_question())

    def check_for_next_question(self):
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.canvas.itemconfig(self.question_text, text="The End")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")
