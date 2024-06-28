from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
raps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global raps
    raps = 0
    if timer is not None:
        window.after_cancel(timer)

    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global raps
    timer_sec = 0
    raps += 1

    if raps == 8:
        timer_sec = LONG_BREAK_MIN * 60
        title_label.config(text="Break", fg=RED)
    elif raps % 2 == 1:
        timer_sec = WORK_MIN * 60
        title_label.config(text="Work", fg=GREEN)
    else:
        timer_sec = SHORT_BREAK_MIN * 60
        title_label.config(text="Break", fg=PINK)

    count_down(2)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        checks = ["✓" for rap in range(raps) if rap % 2 == 0]
        checks_text = "".join(checks)
        check_marks.config(text=checks_text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
check_marks.grid(row=3, column=1)

window.mainloop()
