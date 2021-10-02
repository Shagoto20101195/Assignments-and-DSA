n = int(input("Enter number: "))
ans = ""

while(n > 0):
    ans += str(n % 10)
    n //= 10

if(n == 0):
    print(1)
else:
    print(ans)