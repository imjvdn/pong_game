import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1.5
ball.dy = 1.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function to move the paddles up and down
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

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Flag to track the game state
game_paused = False

# Function to toggle the game state
def toggle_pause():
    global game_paused
    game_paused = not game_paused

# Keyboard bindings
wn.onkeypress(toggle_pause, "p")

# Flag to track the game state
game_paused = False

# Function to toggle the game state
def toggle_pause():
    global game_paused
    game_paused = not game_paused
    
    # Function to restart the game
def toggle_restart():
    global score_a, score_b, game_paused
    score_a = 0
    score_b = 0
    game_paused = False
    ball.goto(0, 0)
    ball.dx = 1.5
    ball.dy = 1.5
    pen.clear()
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Create a turtle to display the pause screen
pause_screen = turtle.Turtle()
pause_screen.speed(0)
pause_screen.color("white")
pause_screen.penup()
pause_screen.hideturtle()
pause_screen.goto(0, 0)

# Keyboard bindings
wn.onkeypress(toggle_pause, "p")
wn.onkeypress(toggle_restart, "r")

# Main game loop
while True:
    wn.update()

    # Check the game state
    if game_paused:
        pause_screen.write("Game Paused,\nPress 'r' to restart", align="center", font=("Courier", 24, "normal"))
        continue  # skip the rest of the loop and go to the next iteration
    else:
        pause_screen.clear()  # clear the pause screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)  # set the ball's vertical position to the top of the border
        ball.dy *= -1  # change the ball's vertical direction

    if ball.ycor() < -290:
        ball.sety(-290)  # set the ball's vertical position to the bottom of the border
        ball.dy *= -1  # change the ball's vertical direction

    if ball.xcor() > 390:
        ball.goto(0, 0)  # reset the ball to the middle of the screen
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)  # reset the ball to the middle of the screen
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        
wn.mainloop()

