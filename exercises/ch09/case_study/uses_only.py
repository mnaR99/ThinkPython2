
# ---- 9.4

def uses_only(word, accepted):
    for letter in word:
        if letter not in accepted:
            return False
    return True


fin = open("./exercises/resources/words.txt")

test = input("Only letters: ").replace(" ", "")

n = 0
accepted = 0
for line in fin:
    n += 1
    word = line.strip()
    if uses_only(word, test):
        accepted += 1
        print(word)
