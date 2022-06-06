
# ---- 10.2

def cumsum(t):
    ct = [t[0]]
    for i in range(1, len(t)):
        ct += [ct[i-1] + t[i]]
    return ct


t = [1, 2, 3]
print(cumsum(t))
