# ---- pp 72

def print_backward(word):
    for letter in word[::-1]:
        print(letter)


print_backward("hello")

# ---- pp 73

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter in ["O", "Q"]:
        letter += "u"

    print(letter + suffix)

# ---- pp 75


def find(word, letter, start_at):
    index = start_at
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


print(find("banana", "n", 3))


def count(word, char):
    count = 0
    for letter in word:
        if letter == char:
            count += 1
    return count


print(count("banana", "a"))


def count(word, char):
    count = 0
    index = 0
    while True:
        pos = find(word, char, index)
        if pos == -1:
            break
        count += 1
        index = pos + 1
    return count


print(count("banana", "a"))
