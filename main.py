import random
import time
from tkinter import *
import pandas

try:
    word_df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_df = pandas.read_csv("data/french_words.csv")

french_list = word_df.to_dict(orient="records")
current_card = {}


def reverse_card():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(french_list)

    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    timer = window.after(3000, reverse_card)


def click_right():
    french_list.remove(current_card)

    new_df = pandas.DataFrame(french_list)
    new_df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

timer = window.after(3000, reverse_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 264, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=(FONT, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT, 60, "bold"))
canvas.itemconfig(card_title, fill="black")
canvas.itemconfig(card_word, fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=click_right)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
