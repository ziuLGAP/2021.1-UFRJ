"""
Lab de Alg. e programação 17
Luiz Guilherme de Andrade Pires - ECI
DRE -> 121070338
data: 24/09/2021
"""

class metodo_newton:
    def __init__(self, coeficientes, x0, n):
        self.coeficientes = coeficientes
        self.x0 = x0
        self.n = n
    
    def func_x(self, x):
        soma = []
        for i in range(len(self.coeficientes)):
            s = self.coeficientes[i] * x ** i
            soma.append(s)
        return sum(soma)
    
    def der_x(self, x):
        soma = []
        for i in range(len(1,self.coeficientes)):
            s = i * self.coeficientes[i] * x ** (i-1)
            soma.append(s)
        return sum(soma)

    def raiz(self):
        xa = self.x0
        xn = 0 
        for _ in range(self.n):
            try:
                xn = xa - (self.func_x(xa)/self.der_x(xa))
                xa = xn
            
            except ZeroDivisionError:
                return ("Abortado")
        
        return (func_x(xa), xa)
       


a = metodo_newton([3,2], 2, 1)
print(a.raiz)


    
        