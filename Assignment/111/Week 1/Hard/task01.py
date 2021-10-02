n = int(input("Enter number: "))
n2 = n
s = ""
count = 0

while(n > 0):
    temp = str(n % 10)
    n //= 10
    
    if(len(s) == 0):
        s += temp
        count += 1
    else:
        check = True
        for i in s:
            if(i == temp):
                check = False
                break
        
        if(check):
            count += 1
            s += temp
            
if(n2 == 0):
    print(1)
else:
    print(count)