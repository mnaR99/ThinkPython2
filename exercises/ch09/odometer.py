
# ---- 9.8

def is_palindrome(s):
    return s == s[::-1]


def odometer_fmt(n):
    """
    Number filled with leading zeros.
    """
    return str(n).zfill(6)


def has_condition(n):
    """
    Last 4 digits are palindrome.
    One mile later, last 5 digits are palindrome.
    One mile later, middle 4 digits are palindrome.
    One mile later, all 6 digits are palindrome.
    """

    if not is_palindrome(odometer_fmt(n)[-4:]):
        return False
    if not is_palindrome(odometer_fmt(n+1)[-5:]):
        return False
    if not is_palindrome(odometer_fmt(n+2)[-5:-1]):
        return False
    if not is_palindrome(odometer_fmt(n+3)):
        return False

    return True


for i in range(int(1e6)):
    if has_condition(i):
        print(odometer_fmt(i))
