
# ---- 3.12

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


def is_interlocked(e, t, n):
    for i in range(n):
        if not in_bisect(e[i::2], t):
            return False
    return True


def interlocked_words(t, n):
    for word in t:
        if is_interlocked(word, t, n):
            for i in range(n):
                print(word[i::2], end=",")
            print(word)


# ----

fin = open("./exercises/resources/words.txt")

t = []

for line in fin:
    word = line.strip()
    t.append(word)

print(interlocked_words(t, 2))
print(interlocked_words(t, 3))
