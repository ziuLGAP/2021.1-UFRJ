"""
Lab. de Alg. e programação Exercício 11
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 20/08/2021
"""

def sum_linhas(cubo):
    for i in range(len(cubo)):
        for j in range(i + 1, len(cubo)):
            if sum(cubo[i]) != sum(cubo[j]):
                return False

            return True

def sum_colunas(cubo): 
    soma = []   
    for x in range(len(cubo[0])):
        nums = []
        for y in range(len(cubo)):
            num = cubo[y][x]
            nums.append(num)
        soma.append(sum(nums))
    
    for i in range(len(soma)):
        for j in range(i + 1, len(soma)):
            if soma[i] != soma[j]:
                return False

            return True

def sum_diagonal(cubo):
    somap = []
    somas = []

    for i in range(len(cubo)):
        num = cubo[i][i]
        somap.append(num)

    for i in range(len(cubo)):
        num = cubo[i][-i - 1]
        somas.append(num)

    if sum(somap) != sum(somas):
        return False
    
    return True
def sumcolunas(cubo):
    soma = []   
    for i in range(len(cubo)):
        num = cubo[i][0]
        soma.append(num)
    return sum(soma)

def sumdiagonal(cubo):
    soma = []

    for i in range(len(cubo)):
        num = cubo[i][i]
        soma.append(num)
    
    return sum(soma)

def main():
    cubo = eval(input("Informe o cubo: "))

    linha = sum(cubo[0])
    coluna = sumcolunas(cubo)
    diagonal = sumdiagonal(cubo)
    if len(cubo) == 1:
        print(True)

    elif sum_colunas(cubo):
        if sum_linhas(cubo):
            if sum_diagonal(cubo):
                if linha == coluna == diagonal:
                    print(True)
                
                else:
                    print(False)
            
            else:
                print(False)
        
        else:
            print(False)
    
    else:
        print(False) 

main()