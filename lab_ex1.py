"""
Lab. de Alg. e programação Exercício 1
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 23/07/2021
"""

def valida_dados(dado):
    """Verifica o dado enviado, retornando True para números inteiros"""
    if (dado.strip("-")).isnumeric():
        return True

    print("Informe um número!!!")
    return False

def multiplica_num():
    """Dobra o número enviado"""
    num = input("Escolha um número: ")
    if valida_dados(num):
        print(2*(int(num)))

multiplica_num()
