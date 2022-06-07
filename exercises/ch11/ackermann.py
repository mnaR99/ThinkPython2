
# ---- 11.3

def ack(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))


memo = {}


def ack_memoized(m, n):
    global memo
    if (m, n) in memo:
        return memo[(m, n)]

    if m == 0:
        res = n+1
    elif m > 0 and n == 0:
        res = ack_memoized(m-1, 1)
    elif m > 0 and n > 0:
        res = ack_memoized(m-1, ack_memoized(m, n-1))

    memo[(m, n)] = res
    return res


print(ack_memoized(3, 4))
print(ack_memoized(3, 7))
