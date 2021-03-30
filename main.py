x = 2


def check(x: int):
    if x == True:
        print("x = True")
        return True
    elif not x:
        print("x = False")
        return False
    else:
        print("x =", x)
        # return x + 5


z = check(x) + check(x)
print(z)
