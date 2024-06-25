from turtle import Turtle, Screen, colormode
import random

# 컬러 추출
# import colorgram

# colors_extract = colorgram.extract('demaen_hirst\'s_spot.jpg', 30)
#
#
# def extract_RGB(color):
#     r, g, b = color.rgb
#     return r, g, b
#
#
# color_list = [extract_RGB(color) for color in colors_extract]
color_list = [
    (184, 44, 67), (216, 160, 85), (235, 203, 92), (230, 220, 225), (13, 126, 172), (3, 171, 217),
    (220, 74, 50), (228, 233, 231), (211, 70, 93), (124, 180, 200), (47, 56, 109), (50, 168, 126),
    (8, 147, 101), (207, 141, 161), (147, 77, 63), (172, 166, 65), (35, 46, 62), (102, 44, 61),
    (114, 176, 122), (30, 56, 49), (145, 206, 229), (220, 171, 183), (4, 106, 73), (8, 92, 108),
    (222, 176, 168), (69, 38, 46), (166, 206, 194), (106, 48, 47)
]

# TODO : 10 x 10 사이즈
# TODO : 각 점의 크기는 20, 점간 간격 50

colormode(255)
t = Turtle()
INTERVAL = 50
DOT_SIZE = 20

t.hideturtle()
t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)
position = t.position()
print(position[0])

for i in range(10 * 10):

    if i != 0 and i % 10 == 0:
        t.setpos(position[0], position[1] + INTERVAL * i / 10)

    t.dot(DOT_SIZE, random.choice(color_list))
    t.fd(INTERVAL)

screen = Screen()
screen.exitonclick()
