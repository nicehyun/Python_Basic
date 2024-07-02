import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score : 0", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(bg="white", highlightthickness=0, width=300, height=250, )
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_img, command=self.click_true_button)
        self.false_button = Button(image=self.false_img, command=self.click_false_button)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="end")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def click_true_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def click_false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
