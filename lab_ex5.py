"""
Lab. de Alg. e programação Exercício 5
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 06/08/2021
"""

def det_1(matriz):
    """retorna o determinante de uma matriz 1x1"""
    return matriz[0][0]

def det_2(matriz):
    """retorna o determinante de uma matriz 2x2"""
    return ((matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0]))

def det_3(matriz):
    """retorna o determinante de uma matriz 3x3"""
    return(((matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][0]) + \
        (matriz[0][2] * matriz[1][0] * matriz[2][1])) - ((matriz[0][0] * matriz[1][2] * matriz[2][1]) + \
        (matriz[0][1] * matriz[1][0] * matriz[2][2]) + (matriz[0][2] * matriz[1][1] * matriz[2][0])))

def main():
    """retorna o determinante da matriz informada"""
    matriz = eval(input("Informe a matriz: "))

    if len(matriz[0]) == 1:
        print(det_1(matriz))
    
    elif len(matriz[0]) == 2:
        print(det_2(matriz))
    
    else:
        print(det_3(matriz))

main()