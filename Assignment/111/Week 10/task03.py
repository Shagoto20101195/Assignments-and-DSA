# Task 03

class RealNumber:
    def __init__(self, r=0):
        self.__realValue = r
    def getRealValue(self):
        return self.__realValue
    def setRealValue(self, r):
        self.__realValue = r
    def ping(self):
        print('I am in RealNumber class')
    def __str__(self):
        return 'RealPart: '+str(self.getRealValue())

class ComplexNumber(RealNumber):
    def __init__(self, n1 = 1.0, n2 = 1.0):
        super().__init__(n1*1.0)
        self.complexValue = n2*1.0
    def __str__(self):
        temp = super().__str__()
        return temp + "\n" +f"ImaginaryPart: {self.complexValue}"
        

cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5,7)
print(cn2)
print('---------')