from tkinter import *

def converter():
   mile = int(input.get())
   to_km = mile * 1.609
   print(to_km)
   conversion.config(text=to_km)

# Create window
window = Tk()
window.title(string="Mile to Km Converter")
# window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

# Input
input = Entry(width=10)
input.grid(column=1, row=0)

# Label
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

# Label
equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=1)

# Label
conversion = Label(text="0")
conversion.grid(column=1,row=1)

# Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=converter)
button.grid(column=1,row=2)

window.mainloop()