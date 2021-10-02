n = input("Enter word: ")
count = 0
ans = ""

for i in n:
    if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        count += 1
    else:
        ans += i
        
print(ans + str(count))