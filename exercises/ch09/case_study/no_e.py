
# ---- 9.2

def has_no_e(word):
    ans = "e" not in word
    return ans


fin = open("./exercises/resources/words.txt")

n = 0
no_e = 0
for line in fin:
    n += 1
    word = line.strip()
    if has_no_e(word):
        no_e += 1
        print(word)


print(
    'Percentage of words in the list that have no "e":',
    round(no_e/n * 100, 2),
    "%"
)
