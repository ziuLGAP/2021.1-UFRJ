"""
Lab. de Alg. e programação Exercício 10
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 20/08/2021
"""


def tamanho(num):
    return len(num)

def revert(num):
    return int(num[::-1])

def main():
    num = input("Informe o número: ")
    print(tamanho(num), revert(num))

main()