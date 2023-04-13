from turtle import Turtle, Screen
from cell import Cell
#window dimensions and title
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TITLE = "Snake"

#create and initialize window
screen = Screen()
screen.setup(WINDOWWIDTH, WINDOWHEIGHT)
screen.title(TITLE)
screen.tracer(0)


snake = Cell(0,0,0,0,0)
screen.exitonclick()

