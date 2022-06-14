
# ----

def sum_all(*args):
    s = 0
    for n in args:
        s += n
    return s


print(sum_all(1, 2, 3))
