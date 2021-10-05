"""
P1 de Alg. e programação Questão 8
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 23/08/2021
"""
def sort(lista):
    mini =  lista.index(min(lista))
    a = 0
    if a == mini:
        a += 1
    
    for b in range(1, len(lista)):
        if lista[a] > lista [b]:
            if b != mini:
                a = b

    x = 0
    for y in range(1, len(lista)):
        if x == mini:
            x += 1
        if x == a:
            x += 1
        if lista[x] > lista[y]:
            if y != mini:
                if y != a:
                    x = y
    
    return[min(lista), lista[a], lista[x], max(lista)]


lista = eval(input("Informe a lista: "))
print(sort(lista))
