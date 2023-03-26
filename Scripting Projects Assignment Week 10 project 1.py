from turtle import Turtle
import math

def drawCircle(t, x, y, radius):
    distance = (2*math.pi*radius) / 120
    t.up()
    t.goto(x, y + radius)
    t.down()

    for i in range(120):
        t.forward(distance)
        t.right(3)

def main():
    radius = 100
    x = 25
    y = 75
    t = Turtle()
    drawCircle(t, x, y, radius)
    t.done()

if __name__ == "__main__":
    main()
