def gen(num):
    x = 0
    while True:
        if (x < num):
            yield x
            x += 1
        else:
            break

def fab(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)

def fab2(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    k0 = 0
    k1 = 1
    s = 0
    i = 1
    while i < n:
        s = k1 + k0
        k0 = k1
        k1 = s
        i += 1

    return s


if __name__ == '__main__':

    g = gen(10)
    for x in g:
        print(x, end = ' ')
    print()

    for x in range(10):
        print(fab(x), end = ' ')
    print()

    for x in range(10):
        print(fab2(x), end = ' ')
    print()


