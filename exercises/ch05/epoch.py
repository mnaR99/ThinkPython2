import time

current = time.time()
factors = [60, 60**2, 60**2 * 24]
periods = ["minutes", "hours", "days"]


def period_since_epoch(time, n):
    if n < 0:
        print(int(time % 60), "seconds")
    else:
        print(int(time // factors[n]), periods[n])
        period_since_epoch(time % factors[n], n-1)


period_since_epoch(current, 2)
