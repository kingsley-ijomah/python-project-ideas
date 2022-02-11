import random
import time
import turtle

delay = 0.1
score = 0
high_score = 0

# setup the screen
screen = turtle.Screen()
screen.title("Snake Game: by kingsley")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24))


# directions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

segments = []  # holds the snake body

while True:
    screen.update()

    # check collision with walls
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        # reset score
        score = 0

        # reset delay
        delay = 0.1

        pen.hideturtle()
        pen.clear()
        pen.write(
            "Score: {} High Score: {}".format(score, high_score),
            align="center",
            font=("Courier", 24),
        )

    # check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # grow snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()

        segments.append(new_segment)

        # shorten the delay
        delay -= 0.001

        # increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.hideturtle()
        pen.clear()
        pen.write(
            "Score: {} High Score: {}".format(score, high_score),
            align="center",
            font=("Courier", 24),
        )

    # move end of segment first in reverse
    for index in reversed(range(len(segments))):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide segments
            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            # reset score
            score = 0

            # reset delay
            delay = 0.1

            pen.hideturtle()
            pen.clear()
            pen.write(
                "Score: {} High Score: {}".format(score, high_score),
                align="center",
                font=("Courier", 24),
            )

    time.sleep(delay)

screen.mainloop()
