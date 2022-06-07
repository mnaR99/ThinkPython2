
# ---- 10.11

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

t = []

for line in fin:
    word = line.strip()
    t.append(word)

for word in t:
    rword = word[::-1]
    if in_bisect(rword, t):
        print(word, rword)
        t.remove(rword)
