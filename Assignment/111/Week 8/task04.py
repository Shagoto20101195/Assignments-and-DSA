# Task 04

class Cat:
    def __init__(self, type1 = None, type2 = None):
        self.color = type1
        self.action = type2
        if(type1 == None and type2 == None):
            self.color = "White"
            self.action = "sitting"
        elif(type1 == None and type2 != None):
            self.color = "White"
        elif(type1 != None and type2 == None):
            self.action = "sitting"
    def changeColor(self, col):
        self.color = col
    def printCat(self):
        print(self.color, "cat is", self.action)

c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()