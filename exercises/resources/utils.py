
def read_words():
    """
    Returns a list of the words in words.txt
    """
    t = list()
    fin = open("./exercises/resources/words.txt")
    for line in fin:
        word = line.strip()
        t.append(word)
    return t
