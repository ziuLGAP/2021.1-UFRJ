"""
Lab de Alg. e programação 16
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 17/09/2021
"""

class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes
    
    def __setitem__(self, grau, coeficiente):
        if grau > len(self.coeficientes):
            for _ in range(grau - len(self.coeficientes)):
                self.coeficientes.append(0)
            self.coeficientes.append(coeficiente)
        
        elif grau < len(self.coeficientes):
                self.coeficientes[grau] = coeficiente
        
        else:
                self.coeficientes.append(coeficiente)
            
    def __getitem__(self, grau):
        try:
            return self.coeficientes[grau]
        except IndexError:
            print("Não existe coeficiente desse grau.")
    
    def grau(self):
        return(f"Esse polinomio é do grau {len(self.coeficientes - 1)}.")
    
    def __mul__(self, other):
        prod = [0]*(len(self.coeficientes)+len(other.coeficientes)-1)
        for i1,j1 in enumerate(self.coeficientes):
            for i2,j2 in enumerate(other.coeficientes):
                prod[i1+i2] += j1*j2
        
        return Polinomio(prod)

    def __add__(self, other):
        if len(self.coeficientes) > len(other.coeficientes):
            for _ in range(len(self.coeficientes)-len(other.coeficientes)):
                other.coeficientes.append(0)
        elif len(other.coeficientes) > len(self.coeficientes):
            for _ in range(len(other.coeficientes)-len(self.coeficientes)):
                self.coeficientes.append(0)
    
        nc = []
        for x, y in zip(self.coeficientes, other.coeficientes):
            n = x + y
            nc.append(n)
        return Polinomio(nc)

    def __sub__(self, other):
        if len(self.coeficientes) > len(other.coeficientes):
            for _ in range(len(self.coeficientes)-len(other.coeficientes)):
                other.coeficientes.append(0)
        elif len(other.coeficientes) > len(self.coeficientes):
            for _ in range(len(other.coeficientes)-len(self.coeficientes)):
                self.coeficientes.append(0)
    
        nc = []
        for x, y in zip(self.coeficientes, other.coeficientes):
            n = x - y
            nc.append(n)
        return Polinomio(nc)

    def avalia(self, x):
        soma = []
        for i in range(len(self.coeficientes)):
            s = self.coeficientes[i] * x ** i
            soma.append(s)
        return sum(soma)

p = eval(input(" "))
q = eval(input(" "))
x = eval(input(" "))
p = Polinomio(p)
q = Polinomio(q)

print(p.avalia(x), q.avalia(x), (p+q).avalia(x), (p-q).avalia(x), (p*q).avalia(x))




