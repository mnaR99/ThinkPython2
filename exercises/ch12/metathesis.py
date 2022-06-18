
# ---- 12.3

from exercises.resources.utils import read_words
from exercises.ch12.anagrams import group_anagrams


def anagram_string_distance(s1: str, s2: str):
    char_diffs = [s1[i] != s2[i] for i in range(len(s1))]
    return sum(char_diffs)


def metathesis_pair(t: list):
    pairs = []

    for word0 in t:
        t0 = t.copy()
        t0.remove(word0)

        for word1 in t0:
            if anagram_string_distance(word0, word1) == 2:
                pairs.append((word0, word1))

        t.remove(word0)

    return pairs


def print_metathesis_pair(t: list):

    d = group_anagrams(t)

    for k, v in d.items():
        if len(v) > 1:
            mp = metathesis_pair(v)
            if len(mp) > 0:
                print(*mp, sep="\n")


if __name__ == "__main__":

    words = read_words()
    print_metathesis_pair(words)
