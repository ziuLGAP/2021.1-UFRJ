"""
Lab. de Alg. e programação Exercício 7
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 13/08/2021
"""

def alfa(vet1, vet2):
    if (len(vet1) or len(vet2)) == 0:
        print(False)
        return True
    
    elif vet1[0] == vet2[0]:
        print(True)
        return True
    
    vet1.pop(0)
    vet2.pop(0)
    return alfa(vet1, vet2)

vet1 = eval(input("Informe o primeiro vetor: "))
vet2 = eval(input("Informe o segundo vetor: "))

alfa(vet1, vet2)

