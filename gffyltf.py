if __name__ == '__main__':
    a = int(input("введите a"))
    b = int(input("введите b"))
    c = a + b
    d = a - b
    v = a * b
    n = a / b
    l = a // b
    k = a % b
    o = a ** b
    print("{} + {} = {}".format(a, b, c))
    print("{} - {} = {}".format(a, b, d))
    print("{} * {} = {}".format(a, b, v))
    print(f"{a} / {b} = {n}")
    print(f"{a} // {b} = {l}")
    print(f"{a} % {b} = {k}")
    print(f"{a} ** {b} = {o}")


