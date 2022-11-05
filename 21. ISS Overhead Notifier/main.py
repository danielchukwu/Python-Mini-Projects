# Python - 3.10
# Topic - API parameters
# Program - Some API's take parameters. We will be working with a sunrise and sunset api 
#           endpoint from https://sunrise-sunset.org/api where we are required to 
#           provide the api endpoint with 2 parameters




# Start Coding
import json
import requests
import datetime as dt
import smtplib
import time

# import for my personal email and password and the recipients
from my_info import my_email, my_pass, recipients_email


def iss_is_overhead():
   r = requests.get(url="http://api.open-notify.org/iss-now.json")
   r.raise_for_status()
   res = r.json()

   # Get latitude & longitude of iss
   iss_lat = float( res["iss_position"]["latitude"]  )
   iss_lng = float( res["iss_position"]["longitude"] )

   # Check if iss is overhead
   if (iss_lat in range(LAT-5, LAT+5)) and (iss_lng in range(LNG-5, LNG+5)):
      return True
   return False


def is_night():
   "Check to see if our current location(lat & lng) has a dark sky which is before sunrise and after sunset "
   global LAT
   global LNG

   LAT = 9.076479
   LNG = 7.398574
   FORMATTED = 0

   parameters = {
      "lat": LAT,
      "lng": LNG,
      "formatted": FORMATTED,
   }

   r = requests.get(url="https://api.sunrise-sunset.org/json", params= parameters)
   r.raise_for_status()
   # print( json.dumps(r.json(), indent=4) )

   # Get sunrise time
   sunrise = r.json()["results"]["sunrise"]         # 12 hour formatted time (showing either AM or PM) by default. if FORMATTED is not set to 0
   sunset  = r.json()["results"]["sunset"]          # 24 hour formatted time 

   # Get sunrise time by the hour
   sunrise = int( sunrise.split('T')[1].split(":")[0] )
   sunset  = int( sunset.split('T')[1].split(":")[0] )

   # Get current date time
   time_now = dt.datetime.now()

   # Check if it's night time (early morning or late evening)
   if (time_now.hour <= sunrise) and (time_now.hour >= sunset):
      return True
   return False


# Mail Time
while True:
   print("Again!")
   time.sleep(60)
   if is_night() and iss_is_overhead():
      with smtplib.SMTP("smtp.gmail.com") as connection:
         connection.starttls()
         connection.login(user=my_email,password=my_pass)
         connection.sendmail(from_addr=my_email, to_addrs=recipients_email, msg="subject: ISS ALERT\n\nThe ISS Satellite is close by ...")
         print("Mail Sent ...🚀")


# Conclusion
# Now in a day the iss satellite goes overhead our location about 4 times, therefore we can just have our above code on a for loop for an entire day and then once it does go overhead given it's night time, we will get an email and then we can hurry outside to see the satellite👩‍🎓.
