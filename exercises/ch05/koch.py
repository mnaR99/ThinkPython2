import turtle


def koch(t, x):
    if x < 3:
        t.fd(x)
        return

    koch(t, x / 3)
    t.lt(60)
    koch(t, x / 3)
    t.rt(120)
    koch(t, x / 3)
    t.lt(60)
    koch(t, x / 3)


def snowflake(t, x):
    koch(t, x)
    t.rt(120)
    koch(t, x)
    t.rt(120)
    koch(t, x)


def cesaro(t, x, angle):
    if x < 3:
        t.fd(x)
        return

    cesaro(t, x / 3, angle)
    t.lt(angle)
    cesaro(t, x / 3, angle)
    t.rt(angle*2)
    cesaro(t, x / 3, angle)
    t.lt(angle)
    cesaro(t, x / 3, angle)


interface = turtle.Turtle()
interface.speed(0)
cesaro(interface, 1000, 85)
turtle.done()
