from turtle import Turtle


class MapState(Turtle):
    def __init__(self, position):
        super().__init__()
        self.post_state()
        self.goto(position)

    def post_state(self):
        self.hideturtle()
        self.penup()
        self.color("black")
