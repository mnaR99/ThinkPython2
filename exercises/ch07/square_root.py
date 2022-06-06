import math


def mysqrt(a):
    x = a/2
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return y


def format_res(n):
    return str(round(n, 11)).ljust(14, " ")


def test_square_root(n):
    print("a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   ---------     ------------  ----")
    for a in range(1, n+1):
        a = float(a)
        s1 = mysqrt(a)
        s2 = math.sqrt(a)
        print(a, end=" ")
        print(format_res(s1), end="")
        print(format_res(s2), end="")
        print(abs(s1-s2))


test_square_root(9)
