from turtle import Turtle, Screen
from cell import Cell
from snake import Snake
from food import Food
from random import Random
import time
#window dimensions and title
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TITLE = "Snake"
game_over = False


#create and initialize window
screen = Screen()
screen.setup(WINDOWWIDTH, WINDOWHEIGHT)
screen.title(TITLE)
screen.tracer(0)
snake = Snake(5)
food = Food()

#movement variables
global x_velocity, y_velocity
x_velocity = 10
y_velocity = 0

def up():
    global y_velocity, x_velocity
    y_velocity = 10
    x_velocity = 0
def down():
    global y_velocity, x_velocity
    y_velocity = -10
    x_velocity = 0
def right():
    global y_velocity, x_velocity
    y_velocity = 0
    x_velocity = 10

def left():
    global y_velocity, x_velocity
    y_velocity = 0
    x_velocity = -10

#listen for key presses
screen.listen()
screen.onkey(up, "w")
screen.onkey(down, "s")
screen.onkey(right, "d")
screen.onkey(left, "a")




#game lopp
while not game_over:
    #move snake
    snake.move(x_velocity, y_velocity)

    #check if snake has eaten
    if snake.has_eaten(food):
        food.set_position()
        snake.grow()

    #check if snake has hit wall
    if snake.has_hit_wall() or snake.has_hit_self():
        game_over = True

    screen.update()
    time.sleep(0.2)


screen.exitonclick()

