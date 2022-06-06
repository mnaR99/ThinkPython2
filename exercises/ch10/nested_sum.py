
# ---- 10.1

def nested_sum(t):
    nsum = 0
    for nt in t:
        nsum += sum(nt)
    return nsum


t = [[1, 2], [3], [4, 5, 6]]

print(nested_sum(t))
