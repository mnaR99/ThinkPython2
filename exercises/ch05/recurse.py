
def recurse(n, s):
    """
    Sum of the first n integers, plus s
    n: value must be greater than or equal to 0
    """

    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)


recurse(3, 0)
