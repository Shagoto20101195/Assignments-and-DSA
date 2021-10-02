def check_palindrome(s):
    s = s.replace(" ", "")
    check = True
    index = 0
    
    while(index < len(s) / 2):
        if(s[index] != s[len(s) - index - 1]):
            check = False
            break
        index += 1
    
    if(check):
        return "Palindrome"
    else:
        return "Not a palindrome"
    
s = input("Enter word: ")
print(check_palindrome(s))