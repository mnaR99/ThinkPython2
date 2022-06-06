
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(36, 60))
print(gcd(24, 30))
print(gcd(36, 25))
