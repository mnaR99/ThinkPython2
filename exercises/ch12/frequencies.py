
# ---- 12.1

from exercises.ch11.lecture import histogram


def most_frequent(text):
    d = histogram(text.replace("\n", ""))
    t = list()
    for key, value in d.items():
        t.append((value, key))

    print("__ __")
    for n, s in sorted(t, reverse=True):
        print(f"{s}: {n}")


if __name__ == "__main__":
    text = """
    Write a function called most_frequent that takes a string and prints the
    letters in decreasing order of frequency. Find text samples from several
    different languages and see how letter frequency varies between languages.
    """

    most_frequent(text)
