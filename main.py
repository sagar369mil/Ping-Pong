from turtle import Screen, time
from paddle import Paddle
from ball import Ball
from scoreboard import Score


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height = 600)
screen.title("Welcome to the Pong game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Score()




screen.listen()
screen.onkey(r_paddle.go_up,  "o")
screen.onkey(r_paddle.go_down, "l")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

''' In game, 'o' is "UP" and 'l' is "Down" for right paddle player. Similiarly, 'w' is "UP" and 's' is "DOWN" for left paddle player'''


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
   
   

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    '''When right paddle player misses the ball, left paddle player gains the score '''

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    '''When left paddle player misses the ball, right paddle player gains the score '''

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


    






screen.exitonclick()