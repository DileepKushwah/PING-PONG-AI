import turtle


screen = turtle.Screen()
screen.title("Ping Pong")
screen.bgcolor("black")

left_line = turtle.Turtle()
left_line.speed(1000)
left_line.color("white")
left_line.penup()
left_line.goto(-290, 200)
left_line.pendown()
left_line.goto(-290, -200)
left_line.hideturtle()

right_line = turtle.Turtle()
right_line.speed(1000)
right_line.color("white")
right_line.penup()
right_line.goto(290, 200)
right_line.pendown()
right_line.goto(290, -200)
right_line.hideturtle()


paddle_a = turtle.Turtle()
paddle_a.speed(1000)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-250, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(1000)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(250, 0)


ball = turtle.Turtle()
ball.speed(1000)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5  # Increased speed
ball.dy = 0.5  # Increased speed

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


screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")

while True:
    screen.update()


    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 190:
        ball.sety(190)
        ball.dy *= -1

    if ball.ycor() < -190:
        ball.dy *= -1

    if ball.xcor() > 290:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -290:
        ball.goto(0, 0)
        ball.dx *= -1

    
    if (ball.dx > 0) and (250 > ball.xcor() > 240) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(240)
        ball.dx *= -1

    if (ball.dx < 0) and (-250 < ball.xcor() < -240) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-240)
        ball.dx *= -1
