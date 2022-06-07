
# ---- 11.1

def make_dict():
    d = dict()
    fin = open("./exercises/resources/words.txt")
    for line in fin:
        word = line.strip()
        d[word] = 0
    return d


print("hippo" in make_dict())
