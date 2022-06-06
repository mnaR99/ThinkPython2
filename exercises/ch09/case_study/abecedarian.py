
# ---- 9.6

def is_abecedarian(word):
    n = len(word)
    for i in range(1, n):
        if word[i] < word[i-1]:
            return False
    return True


fin = open("./exercises/resources/words.txt")

n_abecedarian = 0
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        n_abecedarian += 1

print(f"Number of abecedarian words: {n_abecedarian}")
