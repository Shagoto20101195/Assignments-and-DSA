def check(*x):
    s = "Uppercase character missing, Lowercase character missing, Digit missing, Special character missing"
    
    if(x[0]):
        s = s.replace("Uppercase character missing, ", "")
    if(x[1]):
        s = s.replace("Lowercase character missing, ", "")
    if(x[2]):
        s = s.replace("Digit missing, ", "")
    if(x[3]):
        s = s.replace("Special character missing", "")
    
    if(s.endswith(", ")):
        print(s[0: len(s)-2: 1])
    else:
        print(s)
        
        
s = input("Enter password: ")

c1 = False
c2 = False
c3 = False
c4 = False

for i in s:
    temp = ord(i)
    if(temp >= 65 and temp <= 90):
        c1 = True
    elif(temp >= 97 and temp <= 122):
        c2 = True
    elif(temp >= 48 and temp <= 57):
        c3 = True
    elif(i == "_" or i == "#" or i == "@" or i == "$"):
        c4 = True
        
if(c1 and c2 and c3 and c4):
    print("OK")
else:
    check(c1, c2, c3, c4)