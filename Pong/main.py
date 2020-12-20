import turtle
import os


win = turtle.Screen()
win.title("Pong by @Sriram823")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)


#  SCORE
score_a = 0
score_b = 0


# PADDLE A(player)
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# PADDLE B(auto)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)


#  BALL1
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("square")
ball1.color("white")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 0.3
ball1.dy = -0.3


#  BALL2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("square")
ball2.color("red")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -0.4
ball2.dy = -0.4


# #  BALL3
# ball3 = turtle.Turtle()
# ball3.speed(0)
# ball3.shape("square")
# ball3.color("grey")
# ball3.penup()
# ball3.goto(0, 0)
# ball3.dx = -0.6
# ball3.dy = -0.6
#
#
# #  BALL4
# ball4 = turtle.Turtle()
# ball4.speed(0)
# ball4.shape("square")
# ball4.color("yellow")
# ball4.penup()
# ball4.goto(0, 0)
# ball4.dx = -0.5
# ball4.dy = -0.5


balls = [ball1,ball2]
# add ball3 and ball4 in balls to play with more balls

#  PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 24, "normal"))


#  FUNCTIONS
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#  KEYBOARD BINDING
win.listen()
win.onkeypress(paddle_a_up, "Up")
win.onkeypress(paddle_a_down, "Down")


# MAIN GAME LOOP

while True:
    win.update()

    for ball in balls:
        #  MOVE BALL
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #  BORDER
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            os.system("afplay bounce.wav&")

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            os.system("afplay bounce.wav&")

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))


        # PADDLE AND BALL COLLISIONS
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
            ball.setx(-340)
            ball.dx *= -1
            os.system("afplay bounce.wav&")

        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
            ball.setx(340)
            ball.dx *= -1
            os.system("afplay bounce.wav&")


    #  AI
    closest_ball = balls[0]
    for ball in balls:
        if ball.xcor() > closest_ball.xcor():
            closest_ball = ball

    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
                paddle_b_up()

    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
                paddle_b_down()

