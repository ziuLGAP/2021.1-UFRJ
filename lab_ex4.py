"""
Lab. de Alg. e programação Exercício 4
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 30/07/2021
"""

def getLinha(matriz, n):
    """retorna os valores da linha n da matriz no formato de lista"""
    return [i for i in matriz[n]]

def getColuna(matriz, n):
    """retorna os valores das coluna n da matriz em uma lista"""
    return [i[n] for i in matriz]

def produto_matriz():
    """Calcula o produto das matrizes informadas."""
    mat1 = eval(input("Informe a primeira matriz: "))
    if type(mat1[0]) is list:
       mat1lin = len(mat1)
       mat1col = len(mat1[0])
    else:
        mat1lin = 1
        mat1col = len(mat1)    

    mat2 = eval(input("Informe a segunda matriz: "))
    if type(mat2[0]) is list:
       mat2lin = len(mat2)
       mat2col = len(mat2[0])
    else:
        mat2lin = 1
        mat2col = len(mat2)

    matRes = []
    if mat1lin == mat2col or mat1col == mat2lin:
        if (mat1lin and mat1col == 1) and (mat2lin and mat2col == 1):
            listMult = [x*y for x, y in zip(mat1 , mat2)]

            matRes.append(sum(listMult))

        elif mat1lin == 1:
            listMult = [x*y for x, y in zip(mat1, getColuna(mat2, 0))]

            matRes.append(sum(listMult))

        elif mat1col == 1:
            for i in range(mat1lin):           
                matRes.append([])

                for j in range(mat1col):
                    listmult1 = [getColuna(mat1, j)[0] * mat2[i]]
                    listMult2 = [getColuna(mat1, j)[1] * mat2[i]]

                    matRes.append(listmult1)
                    matRes.append(listMult2)

        else:
            for i in range(mat1lin):           
                matRes.append([])

                for j in range(mat2col):
                    listMult = [x*y for x, y in zip(getLinha(mat1, i), getColuna(mat2, j))]

                    matRes[i].append(sum(listMult))

        print(matRes)

    else:
        print("Erro!")

produto_matriz()