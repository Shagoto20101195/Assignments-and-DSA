n = int(input("Enter list numbers: "))
s = input("Enter element list: ")
s = s.replace(", ", "")

ans = []
for i in range(0, n):
    temp = i + 97
    l = []
    
    for j in range(temp, ord(s[len(s) - 1]) + 1, n):
        l.append(chr(j))
    ans = ans + [l]

print(ans)