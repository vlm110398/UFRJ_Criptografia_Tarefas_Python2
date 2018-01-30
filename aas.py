n = input()
x = 1
exp = 0
while(x<=n):
    a = input()
    t = a
    f = 2
    temp = 1
    while(a != 1):
        while(a%f == 0):
            a /= f
            exp += 1
        if(a%f != 0):
            if(exp != 0):
                print f, exp
                if(f == t):
                    temp = 0
                if(not((t-1)%(f-1) == 0 and f != 2 and exp == 1)):
                   temp = 0
            if(a == 1):
                if(temp == 0):
                    print("NAO")
                else:
                    print("SIM")

                print"---"
            f += 1
            exp = 0
    x += 1
