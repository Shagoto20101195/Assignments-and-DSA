s = input("Enter word: ")

ans = ""
check = False
index = 0

while(index < len(s)):
    ans += s[index]
    if(s.endswith(ans) and index < len(s) - 1):
        check = True
        break
    index += 1
    
if(check and s.count(ans) > 2):
    print(ans)
else:
    print("Not Palindrome Substring")