quantidade = input()
contador = 1
while (quantidade >= contador):
    f = 2
    quantfator = 0
    canRun = 0
    number = input()
    n = number
    carmi = 1
    while (number >= 2):
        while (number % f == 0):
            number = number / f
            quantfator += 1

        while (number % f != 0 and canRun == 0):
            if (quantfator != 0):
                print f, quantfator
                if (n == f):
                    carmi = 0
                if (not ((n - 1) % (f - 1) == 0 and f != 2)):
                    carmi = 0
                quantfator = 0
            f += 1
            if (number < f):
                canRun = 1
    if (number == 1):
        if (carmi == 1):
            print "SIM"
        else:
            print "NAO"
    if (canRun == 1):
        print "---"
        f = 2
    contador += 1