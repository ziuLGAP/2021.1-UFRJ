"""
Lab. de Alg. e programação Exercício 2
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 23/07/2021
"""

def determina_primo(numero):
    """Retorna True caso o número informado for primo"""
    divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            divisores = divisores + 1
            if divisores > 1:
              break

    if divisores > 1:
        return False

    return True

def num_primos():
    """Imprime uma lista com todos os valores primos até o número escolhido"""
    primos = []
    alcance = int(input("Escolha um número: "))

    for num in range(1, alcance + 1):
        if determina_primo(num):
            primos.append(num)

    primos.pop(0)
    print(primos)

num_primos()
