n = input()
x = 1
while(x<=n):
    a,b = input()
    alfa1 = 1
    alfa2 = 0
    beta1 = 0
    beta2 = 1
    mod = b
    print a, "-", alfa1, beta1
    print b, "-", alfa2, beta2
    while(a%b != 0):
        resto = a%b
        quo = a/b
        alfa = alfa1 - (alfa2*quo)
        alfa1 = alfa2
        alfa2 = alfa
        beta = beta1 - (beta2*quo)
        beta1 = beta2
        beta2 = beta
        a = b
        b = resto
        print resto, quo, alfa, beta
    print 0, a/b, "-", "-"
    if(resto==1):
		resultado = alfa%mod
		print resultado
    elif(resto == 0):
		print 0
    print("---")
    x+=1
