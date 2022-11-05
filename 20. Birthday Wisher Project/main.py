# Python - 3.10
# Topic - Birthday Wisher
# Program - 🎂




# Let's Code 💢
import datetime
import re
import smtplib
import pandas 
import random
from my_info import  my_email, my_pass


PATH = "20. Birthday Wisher Project"

# Datetime now
today = datetime.datetime.now()
today_tuple = (today.month, today.day)
# print(f"month: {today_tuple[0]}\nday: {today_tuple[1]}")


# Get CSV row that matches todays month and day
birthdays_csv = pandas.read_csv("./32._ Birthday Wisher Project/birthdays.csv")

# Generate dictionary
birthdays_dict = {(value["month"], value["day"]): [value["name"], value["email"]] \
                  for (index, value) in birthdays_csv.iterrows() if (value["month"], value["day"])}


# Send mail function
def send_mail(letter, send_to_email):
   with smtplib.SMTP("smtp.gmail.com") as connection:
      connection.starttls()
      connection.login(user=my_email, password=my_pass)
      connection.sendmail(from_addr=my_email, to_addrs=send_to_email, msg=f"subject: HBD\n\n{letter}")


# If someones BD is today. send them a mail
if today_tuple in birthdays_dict:
   letter_file_path = f"./{PATH}/letter_templates/letter_{random.randint(1,3)}.txt"
   their_name = birthdays_dict[today_tuple][0]
   their_email = birthdays_dict[today_tuple][1]

   with open(letter_file_path) as file:
      letter = file.read()
      letter = letter.replace('[NAME]', their_name)

   send_mail(letter, their_email)


print("Mail Sent ...✈️")