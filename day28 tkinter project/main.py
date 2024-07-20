from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
check_mark = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global check_mark
    reps = 1
    check_mark = ""

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    if reps == 1 or reps % 2 != 0:
        count_down(WORK_MIN*60)
        timer_label.config(text="Working Time", fg= GREEN)
    elif reps == 8:
        count_down(LONG_BREAK_MIN*60)
        timer_label.config(text="Long Break Time", fg= RED)
    else:
        count_down(SHORT_BREAK_MIN*60)
        timer_label.config(text="Short Break Time", fg= PINK)

    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global check_mark
    count_min = math.floor(count / 60) #round the number
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"

    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") #canvas 수정할 땐 itemconfig 사용해야 함
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 != 0:
            check_mark += "✔"
            check_label.config(text= check_mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# canvas에서 image 중심 설정
# image를 PhotoImage의 형태로 넣어야 함
timer_text = canvas.create_text(100, 130, text="00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 10), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 10), command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(bg=YELLOW, fg=GREEN, font=(20))
check_label.grid(row=3, column=1)

window.mainloop()