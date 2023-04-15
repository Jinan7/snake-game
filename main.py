from turtle import Screen
from snake import Snake
from food import Food
from text import TextBox
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

#text box data
score = 0
score_text = f'score: {score}'
game_over_text = 'Game Over!'
text_box = TextBox(0, WINDOWHEIGHT/2 - 20,score_text)


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
        score += 10
        score_text = f'score: {score}'
        text_box.update(score_text)
        food.set_position()
        snake.grow()

    #check if snake has hit wall or self
    if snake.has_hit_wall() or snake.has_hit_self():
        text_box.update(game_over_text)
        game_over = True

    screen.update()
    time.sleep(0.2)


screen.exitonclick()

