def separador(info, tipo, num):
    j = info.index(tipo)
    a = info[:j]
    b = info[j+1:]
    if num == 'a':
        return a
    if num == 'b':
        return b

class NumeroDecimal:
    def __init__(self, num):
        if "." not in num:
            num = num + "."
        div = num.index(".")
        inteiro = int(num[:div])
        dec = num[div+1:]
        if dec == "":
            dec = 0
        self.int = inteiro
        self.dec = dec
        idec = 0
        if dec != 0:
            for _ in range(len(dec)):
                idec -= 1
        for _ in range(idec * -1):
            inteiro *= 10
        numv = ((inteiro + int(dec), idec))
        self.num = numv
        
    def __add__(self, other):
        n = self.num[0]
        m = other.num[0]
        iv = 0
        if self.num[1] > other.num[1]:
            iv = int(self.num[1]) - int(other.num[1])
            idev = other.num[1]
            for _ in range(iv):
                n = n * 10
        if self.num[1] < other.num[1]:
            iv = int(self.num[1]) - int(other.num[1])
            idev = self.num[1]
            for _ in range(iv):
                m = m * 10
        if self.num[1] == other.num[1]:
            idev = self.num[1]

        num = str(n + m)
        return str(num[:idev] + "," + num[idev:])
    def __sub__(self, other):
        n = self.num[0]
        m = other.num[0]
        iv = 0
        if self.num[1] > other.num[1]:
            iv = int(self.num[1]) - int(other.num[1])
            idev = other.num[1]
            for _ in range(iv):
                n *= 10
        if self.num[1] < other.num[1]:
            iv = int(self.num[1]) - int(other.num[1])
            idev = self.num[1]
            for _ in range(iv):
                m *= 10
        if self.num[1] == other.num[1]:
            idev = self.num[1]

        num = str(n - m)
        return str(num[:idev] + "," + num[idev:])
    def __repr__(self):
        return str(str(self.int) + "," + self.dec)

info = input(" ")
if "+" in info:
    i = separador(info, '+', 'a')
    j = separador(info, '+', 'b')
    a = NumeroDecimal(i)
    b = NumeroDecimal(j)
    print(a+b)

elif "-" in info:
    if info[0] == "-":
        info = info[1:]
    i = separador(info, "-", "a")
    j = separador(info, "-", "b")
    i = "-" + i
    a = NumeroDecimal(i)
    b = NumeroDecimal(j)
    print(a-b)