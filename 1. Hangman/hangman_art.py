def showHangmanArt(chances):
   if (chances == 6):
      print('''
       +---+
       |   |
           |
           |
           |
           |
      ========
      ''')
   elif (chances == 5):
      print('''
       +---+
       |   |
       0   |
           |
           |
           |
      ========
      ''')
   elif (chances == 4):
      print('''
       +---+
       |   |
       0   |
      /    |
           |
           |
      ========
      ''')
   elif (chances == 3):
      print('''
       +---+
       |   |
       0   |
      /|   |
           |
           |
      ========
      ''')
   elif (chances == 2):
      print('''
       +---+
       |   |
       0   |
      /|\  |
           |
           |
      ========
      ''')
   elif (chances == 1):
      print('''
       +---+
       |   |
       0   |
      /|\  |
      /    |
           |
      ========
      ''')
   else:
      print('''
       +---+
       |   |
       0   |
      /|\  |
      / \  |
           |
      ========
      ''')
