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
reps = 0
# Make it global so we can access it later to cancel the timer.
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    # Stop the timer.
    window.after_cancel(timer)
    # Change the text back.
    title.config(text="Timer")
    # Set timer back to 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # Reset check marks.
    check_marks.config(text="")
    global reps
    reps = 0
    


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    # Her solution.
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        countdown(long_sec)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_sec)
        title.config(text="Break", fg=PINK)
    else: # 
        countdown(work_sec)
        title.config(text="Work", fg=GREEN)

    # My solution.
    # Counter cycle: 25, 5, 25, 5, 25, 5, 25, 20. After that it repeats.
    # counter_cycle = (25, 5, 25, 5, 25, 5, 25, 20)
    # for mins in counter_cycle:
    #     countdown(mins)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(counter):
    mins = counter // 60
    secs = counter % 60
    canvas.itemconfig(timer_text, text=f"{mins}:{secs:02}")
    if counter > 0:
        global timer
        timer = window.after(1000, countdown, counter - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps // 2):
            mark += "✔"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Create Image requires a type PhotoImage
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="Squish Me", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()