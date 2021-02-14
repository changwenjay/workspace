def fab(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)


for i in range (1, 15):
    print(fab(i))

