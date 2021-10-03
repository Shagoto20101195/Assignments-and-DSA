# Task 04

class Circle:
    def __init__(self, radius):
        self.__r = radius
    def getRadius(self):
        return self.__r
    def setRadius(self, radius):
        self.__r = radius
    def area(self):
        return 3.141592653589793 * self.__r * self.__r
    def __add__(self, other):
        radius = self.__r + other.__r
        return Circle(radius)

c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" ,c1.area())
c2 = Circle(5)
print("Second circle radius:" ,c2.getRadius())
print("Second circle area:" ,c2.area())
c3 = c1 + c2
print("Third circle radius:" ,c3.getRadius())
print("Third circle area:" ,c3.area())