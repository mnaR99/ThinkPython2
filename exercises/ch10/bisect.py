
# ---- 10.10

def in_bisect(e, t):
    n = len(t)
    if n <= 4:
        return e in t

    if e == t[n//2]:
        return True
    elif e < t[n//2]:
        return in_bisect(e, t[:n//2])
    else:
        return in_bisect(e, t[n//2:])


fin = open("./exercises/resources/words.txt")

t1 = []

for line in fin:
    word = line.strip()
    t1.append(word)

print(in_bisect("hippo", t1))
