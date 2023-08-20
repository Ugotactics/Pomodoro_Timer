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
reps = 0
mark = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    check_label.config(text="")
    canvas.itemconfig(timer_text, text=f"00:00")


def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0:
        work_sec = WORK_MIN * 60
        count_down(work_sec)
        timer_label.config(text="Work")
    elif reps % 2 == 0:
        short_break_sec = SHORT_BREAK_MIN * 60
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    elif reps % 8 == 0:
        long_break_sec = LONG_BREAK_MIN * 60
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global mark
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            mark += "✔"
            check_label.config(text=mark)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.minsize(width=200, height=200)
window.config(padx=110, pady=50, bg=YELLOW)

timer_label = Label(width=5, height=1, fg=GREEN, text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW)
timer_label.grid(row=0, column=1)
timer_label.config(padx=50, pady=50)

check_label = Label(fg=GREEN, font=(FONT_NAME, 10, "bold"), bg=YELLOW)
check_label.grid(row=3, column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(row=2, column=0)
start_button.config(padx=10, pady=10)

reset_button = Button(text="reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)
reset_button.config(padx=10, pady=10)

window.mainloop()
