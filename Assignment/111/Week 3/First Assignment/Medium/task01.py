s = input("Enter word: ")
l_count = 0
u_count = 0

for x in s:
    i = ord(x)
    if(i >= 65 and i <= 90):
        u_count += 1
    else:
        l_count += 1
        
if(u_count > l_count):
    print(s.upper())
else:
    print(s.lower())