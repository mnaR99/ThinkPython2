
# ---- 11.4

def has_duplicates(t):
    memo = {}
    for e in t:
        if e in memo:
            return True
        memo.setdefault(e, 0)
    return False


t1 = [1, 4, "a", 3, 5]
print(has_duplicates(t1))

t2 = ["a", 3, 1, "a"]
print(has_duplicates(t2))

t3 = ["a", 1, 0, 2]
print(has_duplicates(t3))
