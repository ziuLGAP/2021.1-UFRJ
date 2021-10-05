"""
P1 de Alg. e programação Questão 3
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 18/08/2021
"""

def caminho_diagonal(lista):
    caminhos = []
    for linhas in lista:
        if min(linhas) == 1:
            return False

    if lista[-1][-1] == 1 or lista[0][0] == 1:
        return False
    
    for a, b in enumerate(lista):
        for c in range(len(b)):
            if lista[a][c] == 0:
                caminhos.append((a, c))

    for i, j in caminhos[:-1]:
        if not (i + 1, j) in caminhos and not (i, j+1) in caminhos:
            caminhos.remove((i, j))
    
    somatorio = [x + y for x, y in caminhos]

    for x in range(len(somatorio) - 1):
        if somatorio[x + 1] - somatorio[x] > 1:
            caminhos.pop(x + 1)
    print(caminhos)
    print(somatorio)
    somatorio2 = [x + y for x, y in caminhos]
    for x in range(len(somatorio2) - 1):
        if somatorio2[x + 1] - somatorio2[x] != 1:
            return False
    
    return caminhos

lista = eval(input("Informe a lista: "))
print(caminho_diagonal(lista))