
# ---- 8.2

print("banana".count("a"))

# ---- 8.3


def is_palindrome(word):
    return word == word[::-1]


print(is_palindrome("redivider"))

# ---- 8.4


def any_lowercase1(s):
    """
    Returns a boolean based on whether the first letter of s is lowercase.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """
    Always evalute if "c" is lower case, so it always returns True.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """
    Returns a boolean based on whether the last letter of s is lowercase.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """
    Returns a boolean based on whether s contains a lowercase.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """
    Returns a boolean based on whether s is lowercase.
    """
    for c in s:
        if not c.islower():
            return False
    return True

# ---- 8.5


def rotate_chr(c, by):

    if c.isupper():
        index0 = ord("A")
    elif c.islower():
        index0 = ord("a")
    else:
        return c

    indexc = ord(c) - index0
    return chr((indexc + by) % 26 + index0)


def rotate_word(s, by):
    new_s = ""

    for c in s:
        new_s += rotate_chr(c, by)
    return new_s


print(rotate_word("IBM", -1))
print(rotate_word("IBM", -52 - 1))

print(rotate_word("cheer", 7))
print(rotate_word("cheer", 78 + 7))

print(rotate_word("melon", -10))
print(rotate_word("melon", 26 - 10))
