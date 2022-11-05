from cgitb import text
from tkinter import *
from tkinter import font
import requests


PATH = "22. Kanye Quotes App"
QUOTES_ENDPOINT = "https://api.kanye.rest/"   # endpoint for a random kanye quote


def get_quote():
   r = requests.get(url=QUOTES_ENDPOINT)
   # Raise exception if we encounter one
   r.raise_for_status()    
   res = r.json()
   a_quote = res['quote']
   print(a_quote)
   if len(a_quote) < 80:
      canvas.itemconfig(quote_text, text=a_quote, font=("Ariel", 24, "bold"))
   else:
      canvas.itemconfig(quote_text, text=a_quote, font=("Ariel", 15, "bold"))

# create window
window = Tk()
window.title("Kanye says...")
window.config(padx=50, pady=50)


# create canvas
canvas = Canvas(width=300, height=414)

# Background image and text
background_img = PhotoImage(file=f"./{PATH}/BACKGR~1.PNG")
canvas.create_image(150, 207, image=background_img)
canvas.grid(column=0, row=0)
quote_text = canvas.create_text(150, 200, text="Hey drip until they kill you a beat", width=250, font=("Ariel", 24, "bold"), fill="white")


# Button
kanye_emoji = PhotoImage(file=f"./{PATH}/kanye.png")
button = Button(image=kanye_emoji, highlightthickness=0, command=get_quote)
button.grid(column=0, row=1)





# keep window on display
window.mainloop()