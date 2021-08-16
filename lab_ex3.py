"""
Lab. de Alg. e programação Exercício 3
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 30/07/2021
"""

def produto_vetores():
    """retorna o produto dos vetores informados"""
    vetora = eval(input("Informe o primeiro vetor: "))
    vetorb = eval(input("Informe o primeiro vetor: "))
    produtos = []

    for x, y in zip((vetora), (vetorb)):
        produto = int(x) * int(y)
        produtos.append(produto)

    soma = sum(produtos)

    print(soma)

produto_vetores()