import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guess_states = []
while len(guess_states) < 50:
    input_state = screen.textinput(title=f"{len(guess_states)}/50 State Correct",
                                   prompt="What's another state name?").title()

    if input_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guess_states:
                missing_state.append(state)

        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if input_state in all_states:
        guess_states.append(input_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == input_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(input_state)
