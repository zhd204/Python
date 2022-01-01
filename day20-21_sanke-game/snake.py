from turtle import Screen, Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self, n):
        self._segments = []
        self.length = n
        self.create_snake()
        self.head = self._segments[0]
        self.head.color('red')

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, n):
        self._length = n

    @property
    def snake_body(self):
        return self._segments

    def create_snake(self):
        xcor = 0
        for _ in range(self.length):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.resizemode("user")
            segment.shapesize(stretch_wid=0.95, stretch_len=0.95)
            segment.penup()
            segment.goto(xcor, 0)
            self._segments.append(segment)
            xcor -= MOVE_DISTANCE

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move(self):
        for seg_index in range(len(self._segments) - 1, 0, -1):
            xcor = self._segments[seg_index - 1].xcor()
            ycor = self._segments[seg_index - 1].ycor()
            self._segments[seg_index].goto(xcor, ycor)
        self.head.forward(MOVE_DISTANCE)
        print(f"snake cords {self.head.xcor()}, {self.head.ycor()}")
        print(f"snake length {len(self._segments)}")

    def add_snake(self):
        segment = Turtle(shape="square")
        segment.resizemode("user")
        segment.shapesize(stretch_wid=0.95, stretch_len=0.95)
        segment.penup()
        segment.goto(self.snake_body[-1].position())
        self._segments.append(segment)
        segment.color("white")

    def reset_snake(self):
        for segment in self._segments:
            segment.goto(2000, 2000)
        self._segments.clear()
        self.create_snake()
        self.head = self._segments[0]
        self.head.color('red')
