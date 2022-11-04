# Python - 3.10
# Topic - Nato Alphabets
# Program - A simple program that takes a users input and then returns a list of nato words for each letter in the users input

# solution


import pandas

# Fetch Nato Alphabets from csv file
nato_data = pandas.read_csv("./15. Nato Alphabet Project/chapter 26/NATO_P~1.CSV")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}



def generate_phonetics():
   # Receive input from user
   user_input = input("Enter a word: ").upper()
   # convert every letter to a nato list
   try:
      output_list = [nato_dict[letter] for letter in user_input]
   except KeyError:
      print("Sorry, only letters in the alphabet please.")
      generate_phonetics()
   else:
      print(output_list)


generate_phonetics()
