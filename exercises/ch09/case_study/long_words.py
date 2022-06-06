
# ---- 9.1

fin = open("./exercises/resources/words.txt")

for line in fin:
    word = line.strip()
    if len(word.replace(" ", "")) > 20:
        print(word)
