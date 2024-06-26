from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.default_x_coor = position[0]
        self.goto(x=self.default_x_coor, y=position[1])

    def up(self):
        self.goto(self.default_x_coor, self.ycor() + 20)

    def down(self):
        self.goto(self.default_x_coor, self.ycor() - 20)
