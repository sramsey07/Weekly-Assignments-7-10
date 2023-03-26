import turtle

def drawFractalLine(t, distance, angle, level):
    if level == 0:
        t.forward(distance)
    else:
        drawFractalLine(t, distance / 3, angle, level - 1)
        t.left(angle)
        drawFractalLine(t, distance / 3, angle, level - 1)
        t.right(angle * 2)
        drawFractalLine(t, distance / 3, angle, level - 1)
        t.left(angle)
        drawFractalLine(t, distance / 3, angle, level - 1)

def drawKochSnowflake(t, distance, level):
    for i in range(3):
        drawFractalLine(t, distance, 60, level)
        t.right(120)

t = turtle.Turtle()
t.speed('fastest')

drawKochSnowflake(t, 200, 4)

turtle.done()
