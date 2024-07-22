from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("words_to_learn.csv") # csv -> dataframe
except FileNotFoundError:
    original_data = pandas.read_csv("german_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) #cancel flip card when the card is changed
    current_card = random.choice(to_learn)
    german = current_card["German"]
    canvas.itemconfig(canvas_card, image=front_img)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=german, fill="black")
    flip_timer = window.after(5000, func=flip_card) # set new timer for the new card

def flip_card():
    global current_card
    canvas.itemconfig(canvas_card, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    print(len(to_learn))


    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flip_card)

#Canvas
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_card = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="language", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()



window.mainloop()
