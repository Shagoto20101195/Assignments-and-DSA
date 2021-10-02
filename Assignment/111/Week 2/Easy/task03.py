def calculate(x, y, z):
    sum = 0
    for i in range(x, y, 1):
        if(i % z == 0):
            sum += i
    return sum
    
a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))
print(calculate(a, b, c))