"""
Lab de Alg. e programação 12
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 27/08/2021
"""

def buscabinaria(v, x, j, i=0):
    if i > j:
        return -1
    
    m = round((i+j)/2)
    if v[m] < x:
        i = m + 1
        return buscabinaria(v, x, j, i)
    if v[m] > x:
        j = m - 1
        return buscabinaria(v, x, j, i)
    
    return m

lista = eval(input("Informe a lista: "))
j = len(lista) - 1
num = int(input("Informe o valor: "))
print(buscabinaria(lista, num, j))

