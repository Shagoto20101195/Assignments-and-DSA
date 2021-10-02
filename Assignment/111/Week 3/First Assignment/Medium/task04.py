s = input("Enter line: ")

temp = s.find("too good")

if(temp > -1):
    for i in range(0, temp):
        print(s[i], end = "")
    
    print("excellent", end = "")
    
    for i in range(temp + 8, len(s)):
        print(s[i], end = "")
        
else:
    print(s)