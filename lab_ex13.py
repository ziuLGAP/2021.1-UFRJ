"""
Lab de Alg. e programação 13
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 27/08/2021
"""

def buscabinaria(v):
    l = []
    l.append(v[0])
    for x in range(1, len(v)):
        m = 0
        for i in range(len(l)):
            if v[x] <= l[i]:
                l.insert(m, v[x])
            if v[x] > l[i]:
                m += 1 
        
        if m == len(l):
            l.append(v[x])
    return l

lista = eval(input("Informe a lista: "))
print(buscabinaria(lista))
            