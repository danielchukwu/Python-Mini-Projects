# Python - 3.10
# Topic - Pomodora
# Program - Build a Pomodora application that helps you time your work shifts and breaks 

# How it Works!
# Work session - 25 mins
# short break - 5 mins

# after 4 work sessions we get a long break
# long break - 20 mins

# Hit 'start' to begin the countdown

# NOTE: For step by step walk through. Check out the chapter 28 from Note 1 to 7 




# solution



from cgitb import text
import math
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
   window.after_cancel(timer)
   global reps
   reps = 0
   timer_label.config(text="Timer", fg=GREEN)
   canvas.itemconfig(time_text, text="00:00")
   check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
   global reps
   reps += 1

   work_sec = WORK_MIN * 60
   short_break_sec = SHORT_BREAK_MIN * 60
   long_break_sec = LONG_BREAK_MIN * 60

   # If it's the 8th rep:
   if reps % 8 == 0:
      timer_label.config(text="Long Break", fg=RED)
      count_down(long_break_sec)
   # If it's 2nd/4th/6th rep:
   elif reps % 2 == 0:
      timer_label.config(text="Short Break", fg=PINK)
      count_down(short_break_sec)
   # If it's the 1st/3rd/5th/7th rep:
   else:
      timer_label.config(text="Work Session", fg=GREEN)
      count_down(work_sec)
      check_marks.config(text="✔" * (reps // 2))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# Countdown

def count_down(count):                 
   minutes = math.floor(count / 60)     
   seconds = math.floor(count % 60)

   if minutes < 10:
      minutes = f"0{minutes}"
   if seconds < 10:
      seconds = f"0{seconds}"

   time = f"{minutes}:{seconds}"
   canvas.itemconfig(time_text, text=f"{time}")
   if count > 0:
      global timer
      timer = window.after(1000, count_down, count-1)
   else:                             
      start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title(string="pomodora")
window.config(padx=100, pady=50, bg=YELLOW)


# Create Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) 

# Adding image
image_rel_path = "./17. Pomodoro GUI Application Project/tomato.png"
tomato_img = PhotoImage(file=image_rel_path)
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)

# Create text
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Label
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 34, "bold"), bg=YELLOW)
check_marks = Label(bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)
check_marks.grid(column=1, row=2)


# Buttons
start_btn = Button(text="Start", command=start_timer)
reset_btn = Button(text="Reset", command=reset_timer)
start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)






window.mainloop()