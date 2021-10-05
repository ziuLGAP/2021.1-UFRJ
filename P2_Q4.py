class Vetor:
    def __init__(self, a):
        self.lista = []
        for i in range(len(a)):
            self.lista.append(a[i])
        

    def check(self, a):
        self.listau = []
        for i , j in enumerate(a):
            if isinstance(j, int):
                self.listau.append(j)
            
            elif isinstance(j, float):
                if j == float(int(j)):
                    self.listau.append(int(j))
                else:
                    pass

            elif isinstance(j, str):
                if "." in j:
                    if float(j) == float(int(float(j))):
                        self.lista.append(int(float(j)))
                    else:
                        pass
            
                elif j.isnumeric():
                    self.listau.append(int(j))
            
                else:
                    pass
    
        return self.listau
    
    def check2(self, a):
        """checa se todos o elementos da lista são inteiros"""
        x = self.check(a)
        if len(x) == len(a):
            return True
        
        return False
            
                

    def mdc(self):
        """esta função divide todos os números da lista checada por um divisor, caso o resulatado desta divisão de um número inteiro para todos os números, este divisor é colocado na lista do mdc"""
        a = self.check(self.lista)
        if a == []:
            return ()
        a = list(set(a))
        div = 2
        mdcs = []
        while div < max(a):
            b = []
            for i in range(len(a)):
                num = a[i]/div
                b.append(num)
            
            if self.check2(b):
                a = b
                mdcs.append(div)
            else:
                div += 1
        if mdcs == []:
            mdcs = [1]
        
        return tuple(mdcs)



    def __repr__(self):
        return str(self.lista)


a = Vetor([14, 28])
print(a.mdc())

