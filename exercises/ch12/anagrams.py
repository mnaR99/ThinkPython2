
# ---- 12.2

from exercises.resources.utils import read_words


def sort_str(word):
    return "".join(sorted(word))


def group_anagrams(words):
    d = dict()
    for word in words:
        d.setdefault(sort_str(word), []).append(word)
    return d


def print_anagrams(words, min):
    d = group_anagrams(words)
    for v in d.values():
        if len(v) >= min:
            print(v)


def print_anagrams2(words, min):
    d = group_anagrams(words)
    t = list()
    for v in d.values():
        n = len(v)
        if n >= min:
            t.append((n, v))

    for n, s in sorted(t, reverse=True):
        print(f"{n}: {s}")


def print_bingos(min_bingo_set_size):
    t = read_words()
    eight_letters = [word for word in t if len(word) == 8]
    print_anagrams2(eight_letters, min_bingo_set_size)


if __name__ == "__main__":
    t = read_words()

    print("1. _____")
    print_anagrams(t, 9)

    print("2. _____")
    print_anagrams2(t, 9)

    print("3. _____")
    print_bingos(6)
