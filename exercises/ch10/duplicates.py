
# ---- 10.7

def has_duplicates(t):
    for i in range(0, len(t)-1):
        for j in range(i+1, len(t)):
            if t[i] == t[j]:
                return True
    return False


t1 = [[1, 2], 4, "a", [3, 5], [4, 5, 6]]
print(has_duplicates(t1))

t2 = ["a", 3, [1, 2], "a"]
print(has_duplicates(t2))

t3 = ["a", 1, [1, 2], 2]
print(has_duplicates(t3))
