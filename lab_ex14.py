def getLinha(matriz, n):
    """retorna os valores da linha n da matriz no formato de lista"""
    return [i for i in matriz[n]]

def getColuna(matriz, n):
    """retorna os valores das coluna n da matriz em uma lista"""
    return [i[n] for i in matriz]

def produto_matriz(mat1, mat2):
    """Calcula o produto das matrizes informadas."""
    if type(mat1[0]) is list:
       mat1lin = len(mat1)
       mat1col = len(mat1[0])
    else:
        mat1lin = 1
        mat1col = len(mat1)    

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

        return(matRes)

    else:
        return("Erro!")

def soma_matriz(a, b):
    soma = []
    for i in range(len(a)):
        soma_temp = []
        for j in range(len(a[0])):
            sum = a[i][j] + b[i][j]
            soma_temp.append(sum)
        soma.append(soma_temp)
    return soma

def sub_matriz(a, b):
    sub = []
    for i in range(len(a)):
        sub_temp = []
        for j in range(len(a[0])):
            sum = a[i][j] - b[i][j]
            sub_temp.append(sum)
        sub.append(sub_temp)
    return sub

def separador(info, tipo, num):
    j = info.index(tipo)
    a = info[1:j-1]
    b = info[j+2:-1]
    if num == 'a':
        return a
    if num == 'b':
        return b
        

class matriz:
    def __init__(self, n, m, v):
        matriz = []
        num = 0
        mtemp = m
        for x in range(n):
            tempL = []
            for y in range(num, mtemp):
                tempL.append(v[y])
            matriz.insert(x, tempL)
            num += m
            mtemp += m
        self.matriz = matriz
    
    def __add__(self, other):
        return str(soma_matriz(self.matriz, other.matriz))
    def __sub__(self, other):
        return str(sub_matriz(self.matriz, other.matriz))
    def __mul__(self, other):
        return str(produto_matriz(self.matriz, other.matriz)) 
    def __repr__(self):
        return str(self.matriz)

info = input(" ")
if '+' in info:
    a = separador(info, '+', 'a')
    b = separador(info, '+', 'b')
    lista1 = eval(a[4:])
    lista2 = eval(b[4:])
    if len(lista1) == 1:
        lista1 = lista1[0]
    if len(lista2) == 1:
        lista2 = lista2[0]
    a1 = matriz(int(a[0]), int(a[2]), lista1)
    b1 = matriz(int(b[0]), int(b[2]), lista2)
    print(a1+b1)

if '*' in info:
    a = separador(info, '*', 'a')
    b = separador(info, '*', 'b')
    lista1 = eval(a[4:])
    lista2 = eval(b[4:])
    if len(lista1) == 1:
        lista1 = lista1[0]
    if len(lista2) == 1:
        lista2 = lista2[0]
    a1 = matriz(int(a[0]), int(a[2]), lista1)
    b1 = matriz(int(b[0]), int(b[2]), lista2)
    print(a1*b1)

elif '-' in info:
    a = separador(info, '-', 'a')
    b = separador(info, '-', 'b')
    lista1 = eval(a[4:])
    lista2 = eval(b[4:])
    if len(lista1) == 1:
        lista1 = lista1[0]
    if len(lista2) == 1:
        lista2 = lista2[0]
    a1 = matriz(int(a[0]), int(a[2]), lista1)
    b1 = matriz(int(b[0]), int(b[2]), lista2)
    print(a1-b1)
