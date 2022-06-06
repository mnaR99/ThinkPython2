
import turtle
import math


def square(t, length):
    for _ in range(4):
        t.fd(length)
        t.lt(90)


bob = turtle.Turtle()
bob.speed(0)
square(bob, 100)
square(bob, 200)
square(bob, 300)


def polygon(t, n, length):
    angle = 360.0 / n
    for _ in range(n):
        t.fd(length)
        t.lt(angle)


polygon(bob, 3, 100)
polygon(bob, 6, 100)
polygon(bob, 9, 100)


def circle(t, r):
    circ = 2 * math.pi * r
    n = int(circ / 3) + 3
    polygon(t, n, circ / n)


circle(bob, 50)

turtle.mainloop()
