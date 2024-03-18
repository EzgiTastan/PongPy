import turtle
import winsound

#wn=window
wn = turtle.Screen()
wn.title("Pong by @EzgiTastan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#let's keep track the scores
score_a = 0
score_b = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
#This is the speed of animation.

paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#I've seperated the ball's movement into two parts, x axis and y axis
ball.dx = 0.3
ball.dy = -0.3
#d= delta, change.

#pen
pen = turtle.Turtle()
pen.speed(0)
#animation speed, not movement speed.
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#FUNctions :)
def paddle_a_up():
    y = paddle_a.ycor()
    #ycor comes from the turtle module. it moves the y coordinate
    y += 20
    paddle_a.sety(y)
    #(y) is the new y.
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    #ycor comes from the turtle module. it moves the y coordinate
    y += 20
    paddle_b.sety(y)
    #(y) is the new y.
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#KEYBOARD BINDING!!!
wn.listen()
wn.onkeypress(paddle_a_up, "w")
#when the user presses w, call the function "paddle_a_up"
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main game loop is here!
while True:
    wn.update()

    #move the ball!
    ball.setx(ball.xcor() + ball.dx)
    #ball's current x coordinate + delta x (change)
    ball.sety(ball.ycor() + ball.dy)

    #Let's set borders.
    if ball.ycor() > 290:
        ball.sety(290)
        # to bounce back!!!!
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        # it will start from the center, again.
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME)
