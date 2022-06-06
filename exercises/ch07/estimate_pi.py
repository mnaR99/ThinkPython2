import math


def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result


def estimate_pi():
    x = 0
    k = 0
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        y = (x + num/den)

        if abs(y-x) < 1e-15:
            return (1/y)*9801/(2*math.sqrt(2))

        x = y
        k += 1


print(estimate_pi())
print(math.pi)
