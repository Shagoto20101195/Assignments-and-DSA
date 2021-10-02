n = int(input("Enter number: "))

binaryN = ""
while(n > 0):
    temp1 = n % 2
    binaryN = str(temp1) + binaryN
    n //= 2

binaryS = ""
for i in binaryN:
    if(i == "1"):
        binaryS += i
        
binaryS = int(binaryS, 2)
print(binaryS)