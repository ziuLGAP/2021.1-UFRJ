"""
P1 de Alg. e programação Questão 4
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 23/08/2021
"""

def anagrama(a, b):
    """Transforma as palavras em lista com cada caracter, e os ordena,\
        caso as duas listas após a ordenação sejam iguais, ele retorna True"""
    lista = []
    lista[:0] = a
    lista.sort()

    listb = []
    listb[:0] = b
    listb.sort()
    if lista == listb:
        return True
    
    return False

a = input(' ')
b = input(' ')

print(anagrama(a, b))