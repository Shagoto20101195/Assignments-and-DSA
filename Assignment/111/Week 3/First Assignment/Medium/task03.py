s = input("Enter word: ")

start = 0
stop = 0
index = 0
check = True

while(index < len(s)):
    x = ord(s[index])
    if(x >= 65 and x <= 90):
        if(check):
            start = index
            check = False
        else:
            stop = index
            break
    index += 1
    
if(start + 1 == stop):
    print("BLANK")
else:
    print(s[start + 1: stop:])