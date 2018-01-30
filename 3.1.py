n = input()
cont = 1
while(cont <= n):
    a,b,c = input()
    alfa1 = 1
    alfa2 = 0
    beta1 = 0
    beta2 = 1
    print a, "-", alfa1, beta1
    print b, "-", alfa2, beta2
    resto = a % b
    while(a%b != 0):
        quo = a/b
        alfa = alfa1 - (alfa2*quo)
        alfa1 = alfa2
        alfa2 = alfa
        beta = beta1 - (beta2*quo)
        beta1 = beta2
        beta2 = beta
        a = b
        b = resto
        mdc = resto
        print mdc, quo, alfa, beta
        resto = a % b
    if(resto == 0 ):
        print resto, a/b, "-", "-"
        if(c % mdc == 0):
            cl = c / mdc
            x = alfa * cl
            y = beta * cl
            print x, y
            print("---")
        else:
            print("0")
            print("---")
    cont+=1
