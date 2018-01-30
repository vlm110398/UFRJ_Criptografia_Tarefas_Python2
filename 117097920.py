def euc_est (a, b):
    alfa1 = 1
    alfa2 = 0
    beta1 = 0
    beta2 = 1
    print a, "-", alfa1, beta1
    print b, "-", alfa2, beta2
    while (a % b != 0):
        resto = a % b
        quo = a / b
        alfa = alfa1 - (alfa2 * quo)
        alfa1 = alfa2
        alfa2 = alfa
        beta = beta1 - (beta2 * quo)
        beta1 = beta2
        beta2 = beta
        a = b
        b = resto
        print resto, quo, alfa, beta
    print 0, a / b, "-", "-"
    print alfa, beta
    return alfa, beta
def sis_cong(a, b, alfa, beta, m, n):
    congruente = (a*beta*n+b*alfa*m )% (m*n)
    print congruente, m*n
    return congruente, m*n
n = input()
x = 1
while(x<=n):
    cong = []
    mod = []
    cong, mod = input()
    congruente = cong[0]
    modulo = mod[0]
    for index in range(1, len(cong)):
        alfa, beta = euc_est(modulo, mod[index])
        congruente, modulo = sis_cong(congruente, cong[index], alfa, beta, modulo, mod[index])
    print "---"
    x += 1