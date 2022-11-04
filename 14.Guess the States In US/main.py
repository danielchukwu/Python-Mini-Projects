import turtle
import pandas
from states_manager import StateManager


PATH = "14.Guess the States In US"

image = f"./{PATH}/blank_states_img.gif"
screen = turtle.Screen()
screen.setup(730, 510)
screen.addshape(image)
turtle.shape(image)


# objects
state_manager = StateManager()

states_data = pandas.read_csv(f"./{PATH}/50_states.csv")
states = set(states_data.state.to_list())


score = 0
while score != 50:
   answer_state = screen.textinput(title=f"{score}/{len(states_data)} \States Correct", \
                                    prompt="What's another state name?")
   answer_state = answer_state.title()

   if answer_state == "Exit":
      break

   if answer_state in states:
      row = states_data[states_data.state == answer_state]
      x, y = int(row.x), int(row.y)
      score += 1
      state_manager.add_state((x, y), answer_state)
      states.remove(answer_state)


# convert to DataFrame
data_from_set = pandas.DataFrame(stfates)
data_from_set.to_csv("./{PATH}/states_to_learn.csv")


screen.exitonclick()