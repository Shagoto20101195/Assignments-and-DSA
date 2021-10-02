s = input("Enter word: ")

index = 0
check = True
while(index < len(s) / 2):
    if(s[index] != s[len(s) - index - 1]):
        check = False
        break
    index += 1

print(check)