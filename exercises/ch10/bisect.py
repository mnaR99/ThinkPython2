
# ---- 10.10

def in_bisect(e, t):
    n = len(t)
    if n <= 4:
        return e in t
    if e < t[n//2]:
        return in_bisect(e, t[:n//2])
    else:
        return in_bisect(e, t[n//2:])
