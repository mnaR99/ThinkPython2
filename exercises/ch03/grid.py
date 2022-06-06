
# ---- 3.3

def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_hline():
    print("+" + " -" * 4, end=" ")


def print_vline():
    print("|" + " " * 8, end=" ")


def print_hlines():
    do_twice(print_hline)
    print("+")


def print_vlines():
    do_twice(print_vline)
    print("|")


def print_hcells():
    print_hlines()
    do_four(print_vlines)


def print_grid():
    do_twice(print_hcells)
    print_hlines()


print_grid()
