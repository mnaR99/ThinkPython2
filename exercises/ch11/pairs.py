
# ---- 11.5

def rotate_chr(c, by):

    if c.isupper():
        index0 = ord("A")
    elif c.islower():
        index0 = ord("a")
    else:
        return c

    indexc = ord(c) - index0
    return chr((indexc + by) % 26 + index0)


def rotate_word(s, by):
    new_s = ""

    for c in s:
        new_s += rotate_chr(c, by)
    return new_s


fin = open("./exercises/resources/words.txt")

d = {}

for line in fin:
    word = line.strip()
    d[word] = 0

for word in d:
    for i in range(1, 26):
        rtword = rotate_word(word, i)
        if rtword in d:
            print(word, i, rtword)
