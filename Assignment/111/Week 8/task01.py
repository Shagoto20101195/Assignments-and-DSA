# Task 01

class Calculator:
    def __init__(self):
        print("Let's Calculate!")
    def add(self, num1, num2):
        print("Value 1:", num1)
        print("Operator: +")
        print("Value 2:", num2)
        print("Result:", (num1 + num2))
    def substract(self, num1, num2):
        print("Value 1:", num1)
        print("Operator: -")
        print("Value 2:", num2)
        print("Result:", (num1 - num2))
    def multiply(self, num1, num2):
        print("Value 1:", num1)
        print("Operator: *")
        print("Value 2:", num2)
        print("Result:", (num1 * num2))
    def divide(self, num1, num2):
        try:
            print("Value 1:", num1)
            print("Operator: /")
            print("Value 2:", num2)
            print("Result:", (num1 / num2))
        except:
            print("Cannot Divide By Zero")

calculate = Calculator()
num1 = int(input())
operator = input()
num2 = int(input())

if(operator == "+"):
    calculate.add(num1, num2)
elif(operator == "-"):
    calculate.substract(num1, num2)
elif(operator == "*"):
    calculate.multiply(num1, num2)
else:
    calculate.divide(num1, num2)