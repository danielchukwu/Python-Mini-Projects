from flask import Flask, render_template
import random


def get_highscore():
   global high_score
   try:
      with open("data.txt", mode='r') as f:
         return int( f.read() )
   except:
      with open("data.txt", mode='w') as f:
         f.write("0")

def save_highscore():
   with open("data.txt", mode='w') as f:
      f.write(f"{high_score}")



score = 0
mis_guess = 0
high_score = get_highscore()
correct_guess = random.randint(0,9)

home_gifs = [
   "https://www.kibrispdr.org/data/1791/numbers-gif-42.gif", 
   "https://s3.eu-west-2.amazonaws.com/img.creativepool.com/files/candidate/portfolio/full/1592805.gif",
   "https://media.tenor.com/zSKM9NA01cMAAAAC/counting-countdown.gif"
]
lose_gifs = [
   "https://media.giphy.com/media/biJ1jmq9woBMI/giphy.gif", "https://media.giphy.com/media/vVEjKbAUFtZzFzjYbz/giphy.gif",
   "https://media.giphy.com/media/ka6M66Z58QEcXadCd4/giphy.gif", "https://media.giphy.com/media/fwkybR8TAVnva/giphy.gif",
   "https://media.giphy.com/media/xUPGcyTHDO6jeUEuu4/giphy.gif", "https://media.giphy.com/media/ZD1wdrHDYKEYdylH8q/giphy.gif",
   "https://media.giphy.com/media/3kyq37gm7HHWDk9K0p/giphy.gif", "https://media.giphy.com/media/10h8CdMQUWoZ8Y/giphy.gif",
   "https://media.giphy.com/media/rfskmSvktqSoo/giphy.gif", "https://media.giphy.com/media/WvzGVdiVRNq8qtWPKu/giphy.gif"
]
win_gifs = [
   "https://media.giphy.com/media/gd0Dqg6rYhttBVCZqd/giphy.gif", "https://media.giphy.com/media/o75ajIFH0QnQC3nCeD/giphy.gif",
   "https://media.giphy.com/media/QO29TZCWS7wctOyvkB/giphy.gif", "https://media.giphy.com/media/l3q2Z6S6n38zjPswo/giphy.gif",
   "https://media.giphy.com/media/ddHhhUBn25cuQ/giphy.gif", "https://media.giphy.com/media/xNBcChLQt7s9a/giphy.gif",
   "https://media.giphy.com/media/sY1WaSHia8kMM/giphy.gif", "https://media.giphy.com/media/YKtTiAiiMyUc8/giphy.gif",
   "https://media.giphy.com/media/l41lYCDgxP6OFBruE/giphy.gif", "https://media.giphy.com/media/xLR6VXtm3kBZytYw73/giphy.gif",
   "https://media.giphy.com/media/5wWf7H0WTquIU1DFY4g/giphy.gif", "https://media.giphy.com/media/IbOiFIJcSlHW2rgVUa/giphy.gif"
]


# create wsgi
app = Flask(__name__, )


# base route
@app.route('/')
def index():
   global correct_guess

   context = {"score": score, "high_score": high_score,"gif": random.choice(home_gifs)}
   return render_template('index.html', context=context )


# guess route
@app.route("/<int:num>")
def guess(num):
   global score, mis_guess, correct_guess, high_score
   if num == correct_guess:
      score += 1
      mis_guess = 0
      guess_is_correct = True
      gif = random.choice(win_gifs)
      message = "You found me. You win!"

      # update highscore
      if score > high_score:
         high_score = score
         save_highscore()

      # change correct guess
      correct_guess = random.randint(0, 9)
   else:
      mis_guess += 1
      guess_is_correct = False
      gif = random.choice(lose_gifs)
      message = "Too low, try again!"  if num < correct_guess else "Too high, try again!"

      if mis_guess == 3:
         score = 0
         mis_guess = 0
   
   context = {"score": score, "guess_is_correct": guess_is_correct, "message": message, "gif": gif, "mis_guess": mis_guess, "high_score": high_score}
   return render_template('guess.html', context=context)


# Run
if __name__ == '__main__':
   app.run(debug=True)