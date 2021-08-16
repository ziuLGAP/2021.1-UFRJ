"""
Lab. de Alg. e programação Exercício 9
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 13/08/2021
"""

dividendo = eval(input("Informe o dividendo: "))
divisor = eval(input("Informe o divisor: "))
lista = 0

def vasco(dividendo, divisor, lista):
    if (dividendo < divisor):
        if lista == 0:
            print("0")
    
        print(lista)

    else:
        return vasco((dividendo - divisor), divisor, (lista + 1))

vasco(dividendo, divisor, lista)
        

