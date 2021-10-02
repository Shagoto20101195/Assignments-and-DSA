s = input("Enter string: ")

lc = []
uc = []
odd = []
even = []

for i in s:
    temp = ord(i)
    
    if(temp >= 65 and temp <= 90):
        uc.append(i)
    elif(temp >= 97 and temp <= 122):
        lc.append(i)
    else:
        temp2 = int(i)
        if(temp2 % 2 == 0):
            even.append(i)
        else:
            odd.append(i)

lc.sort()
uc.sort()
odd.sort()
even.sort()

ans = ""
for i in lc:
    ans += i
for i in uc:
    ans += i
for i in odd:
    ans += i
for i in even:
    ans += i

print(ans)