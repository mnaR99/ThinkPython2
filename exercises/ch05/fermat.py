
def check_fermat(a, b, c, n):

    if n <= 2:
        print("n must be greater than 2")
        return

    theorem_holds = (a ** n + b ** n == c ** n)

    if theorem_holds:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


def askUser():
    check_fermat(
        int(input("a: ")),
        int(input("b: ")),
        int(input("c: ")),
        int(input("n: "))
    )


askUser()
