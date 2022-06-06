
# ---- 9.5

def uses_all(word, accepted):
    for letter in accepted:
        if letter not in word:
            return False
    return True


fin = open("./exercises/resources/words.txt")

test = input("Include letters: ").replace(" ", "")

n = 0
accepted = 0
for line in fin:
    n += 1
    word = line.strip()
    if uses_all(word, test):
        accepted += 1

print(f"Number of words that use all of [{test}]: {accepted}")
