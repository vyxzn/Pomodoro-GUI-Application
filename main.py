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
checks = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="0:00")
    global checks
    checks = 0
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        big_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        big_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        big_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    time_left = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=time_left)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            global checks
            checks += 1
            temp_string = ""
            for x in range(0, checks):
                temp_string = temp_string + "✔"
            cm_label.config(text=temp_string)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pic)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

big_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
big_label.grid(column=1, row=0)

start_button = Button(text="Start", width=7, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=7, command=reset_timer)
reset_button.grid(column=2, row=2)

cm_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
cm_label.grid(column=1, row=3)





window.mainloop()