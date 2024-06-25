from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
start_coordinates = [(-230, - 100 + 40 * i) for i in range(6)]
is_race_on = False


def make_turtle(race_num):
    list_index = race_num - 1

    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[list_index])

    x, y = start_coordinates[list_index]
    t.goto(x=x, y=y)

    return t


all_turtles = [make_turtle(i) for i in range(1, 7)]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color : ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! the {winner_color} turtle id the winner!")
            else:
                print(f"You've lost! the {winner_color} turtle id the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
