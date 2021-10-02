n = int(input("Enter number: "))
count = 0
for i in range(1,n):
    if(n % i == 0):
        count += 1

if(count == 1):
    print("Prime number")
else:
    print("Not prime number")