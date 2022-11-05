# Python - 3.10
# Topic - Flash Card App
# Program - This is a Flash Card App for learning French




# solution



from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
PATH = "19. Flash Card App"
current_card = None
timer = None


# Use words_to_learn.csv file if it exists
try:                                                                         # <--- 
   data_csv = pandas.read_csv(f"./{PATH}/data/words_to_learn.csv")

# use original csv file
except FileNotFoundError:                                                    # <--- 
   original_data_csv = pandas.read_csv(f"./{PATH}/data/french_words.csv")
   data_list = original_data_csv.to_dict(orient="records")     

# if words_to_learn.csv threw no error
else:                                                                        # <--- 
   data_list = data_csv.to_dict(orient="records")




# ---------------------------- NEXT CARD ------------------------------- # 
def next_card():
   global timer, current_card

   current_card = random.choice(data_list)
   canvas.itemconfig(card_title, text="French", fill="black")
   canvas.itemconfig(card_word, text=current_card["French"], fill="black")
   canvas.itemconfig(card_background, image=card_front_img)

   if timer != None:
      window.after_cancel(timer)
   timer = window.after(3000, func=flip_card)

# ---------------------------- FLIP CARD ------------------------------- # 
def flip_card():
   canvas.itemconfig(card_title, text="English", fill="white")
   canvas.itemconfig(card_word, text=current_card["English"], fill="white")
   canvas.itemconfig(card_background, image=card_back_img)

# ---------------------------- REMOVE CARD ------------------------------- # 

def is_known():
   data_list.remove(current_card)
   next_card()

   # store remaining words in a csv file
   to_learn_words = pandas.DataFrame(data=data_list)
   to_learn_words.to_csv(f"./{PATH}/data/words_to_learn.csv", index=False)           # <--- U






# screen
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)


# Create canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Card Front
card_front_img = PhotoImage(file=f"./{PATH}/images/card_front.png")
card_background = canvas.create_image(400, 261, image=card_front_img)

# Card Back
card_back_img = PhotoImage(file=f"./{PATH}/images/card_back.png")


# Card Front: Adding Text
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 25, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Cross Button
cross_image = PhotoImage(file=f"./{PATH}/images/wrong.png")
unknown_btn = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_btn.grid(column=0, row=1)

# Check Button
check_image = PhotoImage(file=f"./{PATH}/images/right.png")
known_btn = Button(image=check_image, highlightthickness=0, command=is_known)
known_btn.grid(column=1, row=1)


next_card()


# Keep Running
window.mainloop()