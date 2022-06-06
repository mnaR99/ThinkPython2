
# ---- 9.7

def has_condition(s):
    """
    Has three consecutive double letters.
    """
    n = len(s)
    if n < 6:
        return False

    for i in range(n-6):
        if s[i] == s[i+1] and s[i+2] == s[i+3] and s[i+4] == s[i+5]:
            return True
    return False


fin = open("./exercises/resources/words.txt")

for line in fin:
    word = line.strip()
    if has_condition(word):
        print(word)
