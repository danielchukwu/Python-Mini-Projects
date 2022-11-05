# Python - 3.10
# Topic - Password Generator
# Program - Write a program that asks how many letters one wants in a password, 
#           and how many symbols and also how many numbers they want and use that to generate a password

# Expected Simulation

# Welcome to the PyPassword Generator!
# How many letters would you like in your password?
# 5
# How many symbols would you like?
# 2
# How many numbers would you like?
# 1
# RuRho%*9
# %ej*oRuR9

# solution

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
   nr_letters= random.randint(8, 10)
   nr_symbols = random.randint(2, 4)
   nr_numbers = random.randint(2, 4)

   password = []
   password.extend([random.choice(letters) for _ in range(nr_letters)])
   password.extend([random.choice(symbols) for _ in range(nr_symbols)])
   password.extend([random.choice(numbers) for _ in range(nr_numbers)])

   random.shuffle(password) 
   password = ''.join(password)
   return password