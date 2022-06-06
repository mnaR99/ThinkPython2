
def is_triangle(a, b, c):
    if a > b + c:
        print("No")
    elif b > a + c:
        print("No")
    elif c > a + b:
        print("No")
    else:
        print("Yes")


def ask_user():
    is_triangle(
        int(input("a: ")),
        int(input("b: ")),
        int(input("c: "))
    )


ask_user()
