import turtle
from turtle import Screen
import pandas
from map_state import MapState


screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
states_low = []
for low_case in states:
    states_low.append(low_case.lower())


x = data.x.to_list()
y = data.y.to_list()
cord = []
for tup in range(0, len(x)):
    cord.append((x[tup], y[tup]))

data_dict = {
    "state": states_low,
    "cord": cord,
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")
correct_stats = []

while len(correct_stats) < 50:
    screen.title(f"{len(correct_stats)}/50 U.S. States Game")
    answer_state = screen.textinput(title="Guess the state: ",
                                    prompt="What's another state's name?").lower()
    if answer_state == "exit":
        missing_states = [state for state in states_low if state not in correct_stats]
        new_data2 = pandas.DataFrame(missing_states)
        new_data2.to_csv("states_to_learn.csv")
        break
    else:
        for state_index in range(0, len(new_data)-1):
            if answer_state == new_data["state"][state_index]:
                if answer_state in correct_stats:
                    pass
                else:
                    correct_stats.append(new_data["state"][state_index])
                    map_state = MapState(new_data["cord"][state_index])
                    map_state.write(f"{answer_state}", align="center", font=("david", 8, "bold"))


