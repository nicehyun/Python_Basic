from turtle import Turtle

STARTING_POSITIONS = [(0 + -20 * i, 0) for i in range(3)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.segments = []
        self.add_segments()
        self.head = self.segments[0]

    def create_segment(self, position):
        new_snake = Turtle()
        new_snake.penup()
        new_snake.shape("square")
        new_snake.color("white")
        new_snake.goto(position)
        return new_snake

    def add_segments(self):
        self.segments.extend([self.create_segment(position) for position in STARTING_POSITIONS])

    def extend(self):
        current_tail = self.segments[-1]

        new_tail = self.create_segment(current_tail.position())
        self.segments.append(new_tail)

    def move(self):
        segments = self.segments
        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.add_segments()
        self.head = self.segments[0]
