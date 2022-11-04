# Python - 3.10
# Topic - Complete Password Manager GUI Application
# Program - A program that helps manage your passwords for the different websites and applications you sign up on



# Goal: Done ✅



# solution


from tkinter import *
from tkinter import messagebox
from chapter_five import PyPasswordGenerator
import pyperclip
import json


PATH = "18. Password Manager GUI App with Tkinter"


# ---------------------------- SEARCH DATA ------------------------------- #

def search_for_data():
   website = website_entry.get()
   
   # if search is empty
   if len(website) == 0:
      messagebox.showinfo("Oops!", "You can't search for nothing. 😅")

   # fetch data
   try:
      with open(f"./{PATH}/data.json", mode='r') as file:
         data = json.load(file)
   except:
      file = open(f"./{PATH}/data.json", mode='w')
      file.close()
      messagebox.showinfo("Error", "No Data File Found.")
   else:
      if website in data:
         # do something
         email = data[website]['email']
         password = data[website]['password']
         msg = f"Email: {email}\nPassword: {password}"
         messagebox.showinfo(title=website.title(), message=msg)
      else:
         messagebox.showinfo("Error", "No Data File Found.")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
   generated_pass = PyPasswordGenerator.generate_password()
   pyperclip.copy(generated_pass)
   password_entry.delete(0, END)
   password_entry.insert(END, generated_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
   # Get inputs
   app_name = website_entry.get()
   email = email_username_entry.get()
   password = password_entry.get()
   new_data = {
      app_name: {
         "email": email, 
         "password": password
      }
   }

   # If an input field is empty. Show message and return
   if len(app_name) == 0 or len(email) == 0 or len(password) == 0:
      messagebox.showinfo(title="Oops", message="There is an empty input field")
      return
   # Ask user if they are okay with there details
   okay = messagebox.askokcancel(title=app_name, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\
                           Is it ok to save?")
   # If not okay just return. Else continue with the execution below
   if not okay:
      return

   # # Write

   try:
      with open(f"./{PATH}/data.json", mode='r') as file:        # 1 <--- A
         data = json.load(file)                                # fetch data
   except:
      with open(f"./{PATH}/data.json", mode='w') as file:        # 2 <--- A
         json.dump(new_data, file, indent=3)
   else:
      data.update(new_data)                                    # update data

      with open(f"./{PATH}/data.json", mode='w') as file:        # 3 <--- A
         json.dump(data, file, indent=3)                       # write data
   finally:
      # clean up entry/input fields
      website_entry.delete(0, END)
      password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title(string="Password Generator")
window.config(padx=50, pady=50)
# window.minsize()


canvas = Canvas(width=200, height=200)

lock_image = PhotoImage(file=f"./{PATH}/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text="Website:")
email_username_label = Label(text="Email/username:")
password_label = Label(text="Password:")

website_label.grid(row=1, column=0)
email_username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# Entry (input)
website_entry = Entry(width=23)
email_username_entry = Entry(width=38)
password_entry = Entry(width=23)

website_entry.grid(row=1, column=1, )
email_username_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

website_entry.focus()
email_username_entry.insert(0, "daniel@gmail.com")

# Button
search_btn = Button(text="search", width=14, command=search_for_data)      # <---
generate_pass_btn = Button(text="Generate Pass", width=14, command=generate_password)
add_btn = Button(text="Add", width=38, command=save_password)      # 👂Event Listener 

search_btn.grid(row=1, column=2)
generate_pass_btn.grid(row=3, column=2)
add_btn.grid(row=4, column=1, columnspan=2)




window.mainloop()