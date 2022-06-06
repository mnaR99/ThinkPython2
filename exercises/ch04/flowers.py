
# ---- 4.2

import turtle
import math


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def petal(t, r, angle):
    for _ in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    for _ in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)


bob = turtle.Turtle()
bob.speed(0)
flower(bob, 7, 60, 60)

bob.speed(0)
flower(bob, 10, 100, 60)

bob.speed(0)
flower(bob, 13, 150, 60)
turtle.mainloop()
