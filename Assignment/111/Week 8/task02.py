# Task 02

class Customer:
    def __init__(self, name):
        self.name = name
    def greet(self, wish = None):
        if(wish == None):
            print("Hello!")
        else:
            print("Hello {:}!".format(wish))
    def purchase(self, *buy):
        print(self.name + ", you purchased", len(buy), "items(s):")
        for x in buy:
            print(x)

customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")