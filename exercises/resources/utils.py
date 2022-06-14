
def read_words():
    """
    Return a list of the wordss in words.txt
    """
    t = list()
    fin = open("./exercises/resources/words.txt")
    for line in fin:
        word = line.strip()
        t.append(word)
    return t
