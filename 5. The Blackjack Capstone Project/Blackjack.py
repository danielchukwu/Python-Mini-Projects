# Python - 3.10
# Topic - Blackjack Game
# Program - Create a Blackjack Video Game


# RULES
# The Goal: it's to add up your cards to the largest number without going over 21
# cards 
# A: can be 11 or 1, up to you
# K, Q, J: 10

# if the cards in your hand > 21. That's a bust, you lose
# if your score == the dealer score. It's a draw.
# if you = 20 and dealer = 21. Dealer wins
# if dealer card total < 17. Dealer must take another card


# SIMULATION
# Your cards: [9, 10]
# Computer's first card: 8
# Type 'y' to get another card, type 'n' to pass: n
# Your final hand: [9, 10]
# Computer's final hand: [8, 10]
# You Win

# NOTE: pd means player or dealer


# solution
import random
import os
from sys import is_finalizing
from logo import logo

print(logo)

class Player:
   
   def __init__(self, name : str) -> None:
      self.name = name
      self.cards = []
      self.cash = 500

class Blackjack:

   def __init__(self) -> None:
      self.player = Player('Player')
      self.dealer = Player('Dealer')
      self.alpha_value = {'A': 1, 'K': 10, 'Q': 10, 'J': 10}
      self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J']
      self.winner = None
      self.bet_options = {"10": 10, "50": 50, "100": 100, "500": 500}
      self.bet = None
      self.gameover = False

   def play(self):
      if self.bet == None:
         self.pick_a_bet()

      self.generate_cards(2, self.player)
      self.generate_cards(2, self.dealer)

      hit = True
      self.print_hands(show_pand=False)

      while self.winner == None:
         # if user havn't choosen 'stand', he can still choose hit
         if hit == True:
            option = input ("Type 'hit' or 'stand': ")
         else:
            option = 'stand'

         if option.lower() == 'hit':
            # For player 
            self.generate_cards(1, self.player)
            self.print_hands(show_pand=False)

            if (self.get_cards_sum(self.player) > 21):
               break
         elif option.lower() == 'stand':
            # For dealer

            hit = False
            self.generate_cards(1, self.dealer)
            # check if anyone has won
            player_sum, dealer_sum = self.get_cards_sum(self.player), self.get_cards_sum(self.dealer)
            if dealer_sum <= 21: self.print_hands(show_pand=True)
            self.set_winner(player_sum, dealer_sum)

         else:
            continue
      # while ends

      self.finalMessage( p_sum = self.get_cards_sum(self.player), d_sum = self.get_cards_sum(self.dealer) )

   def pick_a_bet(self):
      pick_a_bet = input('Pick a bet 10, 50, 100, 500? \n')
      bet = self.bet_options[pick_a_bet]
      if bet:
         self.bet = bet

   def print_hands(self, show_pand=True):
      # show only players card to him and his card sum
      if show_pand == False:
         print(f'\nyour cards: { self.player.cards } -> { self.get_cards_sum(self.player) }')
         print(f'Computer\'s first card: [{ self.dealer.cards[0] }, ?] -> { self.dealer.cards[0] }')
      else:
         print(f'\nyour cards: { self.player.cards } -> { self.get_cards_sum(self.player) }')
         print(f'Computer\'s first card: { self.dealer.cards } -> { self.get_cards_sum(self.dealer) }')
      
   def get_cards(self, pd):
      return pd.cards

   def generate_cards(self, count, pd):
      gen_cards = []
      for i in range(count):
         gen_cards.append( random.choice(self.cards) )


      # add card to player cards
      pd.cards.extend(gen_cards)      
      
      return gen_cards

   def get_cards_sum(self, pd):
      pd_list = []
      for i in pd.cards:
         if type(i) == type(1):
            pd_list.append(i)
         else:
            # find number --> for type <class 'str'> and... Add to pd_list
            pd_list.append( self.alpha_value[i] )

      return sum( pd_list )

   def set_winner(self, p_sum, d_sum):
      # if p_sum == d_sum: its a draw
      if p_sum == d_sum:
         self.winner = 'draw'
      # if player > 21
      elif d_sum > 21:
         self.winner = self.player
      # if 
      elif p_sum > 21:
         self.winner = self.dealer
      elif d_sum > p_sum:
         self.winner = self.dealer

   def finalMessage(self, p_sum, d_sum):
      print(f'\nYour final hand: {self.player.cards} -> { self.get_cards_sum(self.player) }')
      print(f'Dealers final hand: {self.dealer.cards} -> { self.get_cards_sum(self.dealer) }')

      if self.winner == 'draw':
         print('Push!')
      elif self.winner == self.player:
         print("You win!")
         self.player.cash += self.bet
         self.dealer.cash -= self.bet
      else:
         print('You loose!')
         self.dealer.cash += self.bet
         self.player.cash -= self.bet

      print(f'Your remaining cash: ${self.player.cash}')
      
      # if dealer doesn't have enough money. GameOver
      if self.dealer.cash <= self.bet:
         print(f'Dealers remaining Cash: ${self.dealer.cash}\nDealer doesn\'t have enough cash to continue the game. GAME OVER!')
         self.gameover = True
      else:
         # if you have enough money continue the game, else end it
         if self.player.cash >= self.bet and not self.gameover:
            play_again = input("Would you like to play again, 'y' or 'n'? ")
            if play_again == 'y': 
               self.reset()
               self.play()
         else:
            print('Your balance is not enough to continue the game. GAME OVER!')

   def reset(self):
      self.player.cards, self.dealer.cards = [], []
      self.winner = None
      os.system('cls')
      print(f'Your remaining cash: ${self.player.cash}')
      print(f'Dealers remaining cash: ${self.dealer.cash}')



new_game = Blackjack()
new_game.play()