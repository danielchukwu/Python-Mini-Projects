# Python - 3.10
# Topic - caecer cipher
# Program - write a program that encodes and decodes a message

# print ascii art of caecer cipher

# Type 'encode' to encrypt, type 'decode' to decrypt:
# encode
# Type your message:
# hellocoders
# Type the shift number:
# 9
# Here's the encoded result: qnuuxlxmnbc
# Type 'yes' if you want to go again. Otherwise type 'no'.
# yes

# Type 'encode' to encrypt, type 'decode' to decrypt:
# decode
# Type your message:
# qnuuxlxmnbc
# Type the shift number:
# 9
# Here's the decoded result: hellocoders
# Type 'yes' if you want to go again. Otherwise type 'no'.


# solution
import logo

print(logo.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_len = len(alphabet)

def fixIndex(i):
   if i > alphabet_len:
      i %= alphabet_len
      print(i)
   elif i < 0:
      i %= alphabet_len
      print(i)

   return i


# helper function for encoding and decoding
def cipher(text, shift, direction):
   cipher_text = ''

   # find index of text
   for letter in text:
      try:
         if direction == 'encode':
            i = alphabet.index(letter) + shift 
         else:
            i = alphabet.index(letter) - shift
      except:
         i = None

      # fix index if it is ever out of range
      i = fixIndex(i)
      
      if i != None:
         cipher_text += alphabet[i]
      else:
         cipher_text += letter

   print(f'Here\'s the {direction}d result: {cipher_text}')


ride_on = True
while ride_on:
   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
   text = input("Type your message:\n").lower()
   shift = int(input("Type the shift number:\n"))

   if direction.lower() == 'encode':
      cipher(text, shift, direction)
   elif direction.lower() == 'decode':
      cipher(text, shift, direction)

   # ask user if they would like to repeat
   opt = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
   ride_on = True if opt == 'yes' else False