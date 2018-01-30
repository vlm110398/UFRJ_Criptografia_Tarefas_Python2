import math
n = input()
lista = []
l = 3

while (l <= n):
    lista.append(l)
    l += 2

print lista
raiz = int(math.sqrt(n))
print raiz

eliminados = lista[0]
posic_primo = 0
aux_Lista = lista[:]

while (eliminados < raiz):
    nums_Elim = []
    corte1 = eliminados ** 2
    index_Corte1 = aux_Lista.index(corte1)
    print eliminados, corte1, index_Corte1
    aux = index_Corte1

    while (aux < len(aux_Lista)):
        nums_Elim.append(lista[aux])
        aux_Lista[aux] = 0
        aux += eliminados

    primos = filter(bool, aux_Lista)
    print filter(bool, nums_Elim)
    print primos
    posic_primo += 1
    eliminados = primos[posic_primo]

primos.insert(0, 2)
print primos