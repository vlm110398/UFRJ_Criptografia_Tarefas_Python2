x = 1
n = input()
while (x <= n):
    x += 1
    a, e, m = input()
    e %= m-1
    print e
    r = 1
    while (e != 0):
        if (e % 2 == 1):
            print r, a, e, "S"
            r = (r * a) % m
            e = (e - 1) / 2
            a = (a * a) % m
        elif (e % 2 == 0):
            print r, a, e, "N"
            e = e / 2
            a = (a * a) % m

    print r, a, e, "N"
    print"---"
