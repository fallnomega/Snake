import turtle as t

MOVE_DISTANCE = 20
STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_COORDINATES:
            segment = t.Turtle()
            segment.penup()
            segment.color("white")
            segment.shape("square")
            segment.goto(position)
            self.segments.append(segment)
            self.head = self.segments[0]


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

    def extend_snake(self):
        new_segment = t.Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        self.segments.append(new_segment)
        # new_segment.goto(position)
