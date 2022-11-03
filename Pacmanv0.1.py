import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Pacman")
wn.setup(width=600, height=600)

pacman = turtle.Turtle()
pacman.shape("circle")
pacman.color("yellow")
pacman.speed(0)

ghosts = []

for i in range(3):
    ghosts.append(turtle.Turtle())

for ghost in ghosts:
    ghost.shape("circle")
    ghost.color("red")
    ghost.speed(0)
    ghost.penup()
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    ghost.goto(x, y)

ghostspeed = 20



def move(direction):
    if direction == "up":
        y = pacman.ycor()
        pacman.sety(y + 20)

    if direction == "down":
        y = pacman.ycor()
        pacman.sety(y - 20)

    if direction == "left":
        x = pacman.xcor()
        pacman.setx(x - 20)

    if direction == "right":
        x = pacman.xcor()
        pacman.setx(x + 20)


turtle.listen()
turtle.onkey(lambda: move("up"), "w")
turtle.onkey(lambda: move("down"), "s")
turtle.onkey(lambda: move("left"), "a")
turtle.onkey(lambda: move("right"), "d")

while True:
    for ghost in ghosts:
        ghost.forward(20)

        if ghost.xcor() > 290:
            ghost.setx(290)
            ghost.right(60)

        if ghost.xcor() < -290:
            ghost.setx(-290)
            ghost.right(60)

        if ghost.ycor() > 290:
            ghost.sety(290)
            ghost.right(60)

        if ghost.ycor() < -290:
            ghost.sety(-290)
            ghost.right(60)

turtle.mainloop()
