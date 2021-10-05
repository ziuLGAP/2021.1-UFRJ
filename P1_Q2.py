"""
P1 de Alg. e programação Questão 2
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 23/08/2021
"""

lista = eval(input("Informe a lista: "))
index = int(input("Informe o index: "))

def particiona(lista, i):
    """Rearranja os elementos de uma lista 'lista' de tal forma que o elemento originalmente em lista[i], onde lista[i] == x digamos, é movido para a posição j,\
        todos elementos menores que x são movidos para posições menores que j, e todos os elementos maiores ou iguais a x são movidos para posições maiores que j."""
    menores = []
    maiores = []

    for j in range(len(lista)):
        if lista[j] < lista[i]:
            menores.append(lista[j])
        if lista[j] > lista[i]:
            maiores.append(lista[j])
        else:
            pass
    
    menores.append(lista[i])
    nova_lista = menores + maiores
    novo_i = nova_lista.index(lista[i])
    
    del lista[0:]
    for x in range(len(nova_lista)):
        lista.append(nova_lista[x])

    return novo_i


print(particiona(lista, index), lista)
