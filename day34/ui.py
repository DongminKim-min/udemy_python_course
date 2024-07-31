from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quiz_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="sample text",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.get_next_question()

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0,
                                  command=self.is_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,
                                   command=self.is_false)
        self.false_button.grid(row=2, column=1)

        self.score_label = Label(text=f"score:{self.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right:bool):
        self.score = self.quiz.score
        self.score_label.config(text=f"score:{self.score}")

        if is_right is True:
            self.canvas.config(bg="green")
            self.window.after(1000, func=self.get_next_question) # erase the parenthesis of the function!!!

        else:
            self.canvas.config(bg="red")
            self.window.after(1000, func=self.get_next_question)

