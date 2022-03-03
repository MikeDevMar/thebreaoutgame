from turtle import Turtle, Screen
import random
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800,height=500)
screen.tracer(0)
#PLAYER Settings
player = Turtle(shape='square')
player.shapesize(stretch_len=4, stretch_wid=0.5)
player.color('red')
player.hideturtle()
player.penup()
player.goto(0,-225)
player.showturtle()
screen.bgcolor('black')
player.speed(30)
score = Scoreboard()
def go_right():
    new_x = player.xcor()+50
    player.goto(new_x,player.ycor())
def go_left():
    new_x = player.xcor()-50
    player.goto(new_x, player.ycor())
screen.listen()
screen.onkey(go_right,'Right')
screen.onkey(go_left, 'Left')


#Ball Settings
ball = Turtle(shape='circle')
ball.color('green')
ball.shapesize(0.5, 0.5)
ball.penup()
ball.goto(0,-150)
ball_x_move = 5
ball_y_move = 5
ball_move_speed = 0.1

def move_ball():
    ball_new_x = ball.xcor()+ ball_x_move
    ball_new_y = ball.ycor() + ball_y_move
    ball.goto(ball_new_x,ball_new_y)

def ball_y_bounce():
    global ball_y_move, ball_move_speed

    ball_y_move = ball_y_move *-1
    ball_move_speed *= 0.5

def ball_x_bounce():
    global ball_x_move, ball_move_speed
    ball_x_move = ball_x_move * -1
    ball_move_speed *= 0.5

def reset_ball_position():
    global ball_move_speed
    ball.goto(0,-200)
    ball_move_speed = 1

#the food
colors = ['white', 'red', 'blue', 'green', 'yellow', 'brown']
food_list =[]
food_xcor = -380
food_ycor = 0
for r in range (10):
    for i in range(19):
        i_color = random.choice(colors)
        i = Turtle(shape='square')
        i.color(i_color)
        i.penup()
        i.shapesize(stretch_len=2, stretch_wid=0.5)
        i.goto(food_xcor, food_ycor)
        food_xcor+= 42
        food_list.append(i)
    food_ycor+=15
    food_xcor=-380

game_is_on = True
while game_is_on:
    time.sleep(ball_move_speed)
    screen.update()
    move_ball()
    if ball.distance(player) < 25 and ball.xcor()>-380 :
        ball_y_bounce()

    if ball.ycor()>230:
        ball_y_bounce()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball_x_bounce()
        move_ball()

    if ball.ycor()<-240:
       game_is_on= False

    for element in food_list:
        if ball.distance(element) < 20:
            ball_y_bounce()
            element.goto(900, 900)
            score.add_score()

screen.exitonclick()