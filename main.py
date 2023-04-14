from turtle import Turtle, Screen
from cell import Cell
from snake import Snake
import time
#window dimensions and title
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TITLE = "Snake"

#create and initialize window
screen = Screen()
screen.setup(WINDOWWIDTH, WINDOWHEIGHT)
screen.title(TITLE)
screen.tracer(0)
snake = Snake(5)

#game lopp
while True:
    snake.move(20,0)
    screen.update()
    time.sleep(0.2)


screen.exitonclick()

