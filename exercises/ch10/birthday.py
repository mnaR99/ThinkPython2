
# ---- 10.8

from random import randint


def sim_class(size):
    bds = [randint(1, 365)]
    for _ in range(size-1):
        bd = randint(1, 365)
        if bd in bds:
            return True
        bds += [bd]
    return False


def sim_prob(n, size):
    sm = 0
    for _ in range(int(n)):
        sm += sim_class(size)
    return sm/n


print(sim_prob(5e3, 23))
print(sim_prob(5e3, 23))
print(sim_prob(5e3, 23))
