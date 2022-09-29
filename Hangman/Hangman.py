# Python - 3.10
# Topic - Print & Input
# Program - Write a program of hangman

# beekeepe_
#  +---+
#  |   |
#  0   |
# /|\  |
# / \  |
#      |
# ========

# Guess a letter: 


# solution

import random
from hangman_art import *
from hangman_words import *

def hangman_game(words):
   print(logo)   # logo is gotten from the HangmanArt import
   guess = random.choice(words)
   length = len(guess)
   chances = 6
   hidden = ['_'] * length

   del length

   # print(f"{guess}\n{length}\n{hidden}")
   while (chances > 0 and hidden.count('_') > 0):
      # print hidden and hangman
      print(''.join(hidden))
      showHangmanArt(chances)

      your_pick = input('Guess a letter: ')

      # continue if letter was already guessed
      if your_pick in hidden:
         print('you already guessed this letter!')
         continue

      if guess.count(your_pick) == 1:
         i = guess.index(your_pick)
         hidden[i] = your_pick

      elif guess.count(your_pick) > 1:
         # get all indexes
         count = -1
         for letter in guess:
            count += 1
            if letter == your_pick:
               hidden[count] = your_pick
      else:
         chances -= 1
      

   if (chances > 0): 
      print('You win.')
      showHangmanArt(chances)
   else:
      print('You loose.')

hangman_game(word_list)  # word_list gotten from import hangman_words 