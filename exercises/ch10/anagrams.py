
# ---- 10.6

def is_anagram(a, b):
    return sorted(a) == sorted(b)


print(is_anagram("abba", "baba"))
print(is_anagram("gato", "gota"))
print(is_anagram("hola", "lona"))
