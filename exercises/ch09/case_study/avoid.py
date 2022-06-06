
# ---- 9.3

def avoids(word, forbidden):
    for letter in forbidden:
        if letter in word:
            return False
    return True


fin = open("./exercises/resources/words.txt")

test = input("Forbidden letters: ").replace(" ", "")

no_forbidden = 0
for line in fin:
    word = line.strip()
    if avoids(word, test):
        no_forbidden += 1
        print(word)

print(f"Number of words that don't contain any of [{test}]: {no_forbidden}")
