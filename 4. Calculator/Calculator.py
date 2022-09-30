# Python - 3.10
# Topic - Calculator
# Program - Write a calculator program that adds, subtracts, divides and multiplies continously as the user desires

# 25 and 15
# print logo for calc

# what's the first number?: 5
# +
# -
# *
# /
# Pick an operation: /
# What's the next number?: 2
# 5 / 2 = 2.5
# Type 'y' to continue calculating with 2.5, or type 'n' to start a new calculation: y

# Pick an operation: +
# What's the next number?: 6
# 2.5 + 6 = 8.5
# Type 'y' to continue calculating with 2.5, or type 'n' to start a new calculation: n
# import os
# os.system('clr')


# solution 👇✅
from mimetypes import init
from logo import logo


class Calculator:

   def __init__(self) -> None:
      print(logo)
      self.done = False
      self.hold_next_first_num = None

   # used by operations = {}
   def add(a, b): return a + b
   def subtract(a, b): return a - b
   def divide(a, b): return a / b
   def multiply(a, b): return a * b

   operations = {
      "+": add,
      "-": subtract,
      "/": divide,
      "*": multiply
   }

   def calculate(self, first_num : float, op, last_num : float):
      """Calculate the first number and last number using the op(operator)   """
      # perform calculation
      result = self.operations[op](first_num, last_num)

      # return result 
      return result

   def take_input(self):
      """
      Recieves first number, operator and last number from user
      """
      if self.hold_next_first_num == None:
         first_num = float( input("What's the first number?: ") )
         print("+\n-\n*\n/")
      else:
         first_num = self.hold_next_first_num

      op = input("Pick an operation: ")
      last_num = float( input("What's the next number?: ") )

      return first_num, op, last_num


   def start(self):

      while not self.done:
         # recieve input from user and calculate
         first_num, op, last_num = self.take_input()
         result = self.calculate(first_num, op, last_num)
         print(f"{first_num} {op} {last_num} = {result}")
         option = input("Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

         if option == 'y':
            self.hold_next_first_num = result
         else:
            # stop program
            self.done = True

Calculator().start()