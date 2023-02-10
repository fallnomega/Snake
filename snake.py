import turtle as t

MOVE_DISTANCE = 20
STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_COORDINATES:
            self.add_snake(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() == 270:
            return
        else:
            self.head.setheading(90)
        return

    def move_down(self):
        if self.head.heading() == 90:
            return
        else:
            self.head.setheading(270)
        return

    def turn_left(self):
        if self.head.heading() == 0:
            return
        else:
            self.head.setheading(180)
        return

    def turn_right(self):
        if self.head.heading() == 180:
            return
        else:
            self.head.setheading(0)
        return

    def add_snake(self, position):
        new_segment = t.Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_snake(self.segments[-1].position())
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
