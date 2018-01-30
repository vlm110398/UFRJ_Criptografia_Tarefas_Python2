import sys
def potmodular(a, e, m):
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
    return r
x = 1
w = input()
while (x <= w):
    x += 1
    check = 1
    n, b = input()
    k = 0
    q = n-1
    while(q%2 == 0):
        k += 1
        q /= 2
    print k, q
    t = potmodular(b, q, n)
    print q, t
    if(t== 1 or t == n-1):
        print("INCONCLUSIVO")
        print("---")
        check = 0
    i = 1
    u = q
    if(check != 0):
        while(i<k and t != n-1 and t != 1):
            t = t**2 % n
            u *= 2
            print u, t
            i += 1
        if(t == n-1):
            print("INCONCLUSIVO")
            print("---")
        else:
            print("COMPOSTO")
            print("---")
