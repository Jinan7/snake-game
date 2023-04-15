from turtle import Turtle

class TextBox(Turtle):
    def __init__(self, x, y, text):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(text, move=False, align='center', font = ('Arial', 10, 'normal'))

    def update(self, text):
        self.clear()
        self.write(text, move=False, align='center', font=('Arial', 8, 'normal'))