n = int(input("Enter number: "))
var1 = 0
var2 = 1
print(var1, end = " ")
print(var2, end = " ")

total = 0
while(total <= n):
    total = var1 + var2
    if(total <= n):
        print(total, end = " ")
    
    var1 = var2
    var2 = total