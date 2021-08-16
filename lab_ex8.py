"""
Lab. de Alg. e programação Exercício 8
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 13/08/2021
"""

vetor1 = eval(input("Informe o primeiro vetor: "))
vetor2 = eval(input("Informe o segundo vetor: "))
nums = []

def alfa(vet1, vet2):
    if (vet1[:1]) == (vet2[:1]):
        nums.append(vet2[:1])

        return alfa(vet1[1:], vet2[1:])

    if len(vet1) == 0:
        return nums
    
    if len(vet2) == 0:
        return alfa(vet1[1:], vetor2)
    
    elif vet1[:1] != vet2[:1]:
        return alfa(vet1, vet2[1:])

alfa(vetor1, vetor2)

if len(nums) == len(vetor1):
    print(True)
else:
   print(False)