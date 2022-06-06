
# ---- 10.9

import timeit

# ----

start = timeit.default_timer()
fin = open("./exercises/resources/words.txt")
t1 = []

for line in fin:
    word = line.strip()
    t1.append(word)

stop = timeit.default_timer()
print('Time 1: ', stop - start)

# ----

start = timeit.default_timer()
fin = open("./exercises/resources/words.txt")
t2 = []

for line in fin:
    word = line.strip()
    t2 = t2 + [word]

stop = timeit.default_timer()
print('Time 2: ', stop - start)
