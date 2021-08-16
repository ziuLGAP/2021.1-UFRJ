"""
Lab. de Alg. e programação Exercício 6
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 06/08/2021
"""

import copy 

def det3(matriz):
    """Retorna o determinante de uma matriz 3 x 3"""
    return(((matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][0]) + \
        (matriz[0][2] * matriz[1][0] * matriz[2][1])) - ((matriz[0][0] * matriz[1][2] * matriz[2][1]) + \
        (matriz[0][1] * matriz[1][0] * matriz[2][2]) + (matriz[0][2] * matriz[1][1] * matriz[2][0])))

def cof(matriz, num):
    """Retorna o cofator de uma matriz 4 x 4"""
    mat2 = copy.deepcopy(matriz)
    
    for x in range(len(matriz)):
        mat2[x].pop(0)
    
    mat2.pop(num)
    b = det3(mat2)
    return ((-1) ** num) * b

def det4(matriz):
    """Retorna o determinante de uma matriz 4 x 4"""
    Det = 0
    
    for b in range(len(matriz)):
        Det += matriz[b][0] * cof(matriz,b)
    
    return Det 

def cofn(matriz, num):
    """Reduz uma matriz N x N até uma matriz 4 x 4 para calcular seus cofatores"""
    mat2 = copy.deepcopy(matriz)

    for x in range(len(matriz)):
        mat2[x].pop(0)
    mat2.pop(num)
    
    if len(mat2) > 4:
        return ((-1) ** num) * detn(mat2)
    
    elif len(mat2) == 4:
        return ((-1) ** num) * det4(mat2)

def detn(matriz):
    "Retorna o Determinante de uma matriz N x N"
    Determinante = 0
    
    for k in range(len(matriz)):
        Determinante += matriz[k][0] * cofn(matriz,k)
    
    return Determinante

def main():
    """Função principal"""
    matriz = eval(input("Informe a matriz: "))
    if len(matriz) == 4:
        print(det4(matriz))

    else:
        print(detn(matriz))

main()