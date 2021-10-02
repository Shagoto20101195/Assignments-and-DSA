def divide(x, y):
    if(x == 0 or y == 0):
        return 0
    else:
        return (a % b / b)
        
a = int(input("Enter number: "))
b = int(input("Enter number: "))
print(divide(a, b))