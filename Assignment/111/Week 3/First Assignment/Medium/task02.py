s = input("Enter word: ")

n_count = 0
l_count = 0

for i in s:
    x = ord(i)
    
    if((x >= 65 and x <= 90) or (x >= 97 and x <= 122)):
        l_count += 1
    else:
        n_count += 1

if(l_count == 0):
    print("NUMBER")
elif(n_count == 0):
    print("WORD")
else:
    print("MIXED")