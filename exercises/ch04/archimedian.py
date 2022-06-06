
# ---- 4.5

import turtle


def spiral(t, n, length, a, b):
    theta = 0

    for _ in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)

        t.lt(dtheta)
        theta += dtheta


# create the world and bob
bob = turtle.Turtle()
bob.speed(0)
spiral(bob, 1000, 2, 1e-2, 5e-3)
turtle.done()
