def correction(s):
    index = 0
    ans = ""
    sign = 0
    while(index < len(s)):
        if(ord(s[0]) >= 97 and ord(s[0]) <= 122 and index == 0):
            ans += s[0].upper()
        elif(s[index] == "." or s[index] == "!" or s[index] == "?"):
            sign = 1
            ans += s[index]
        elif((ord(s[index]) >= 97 and ord(s[index]) <= 122) and sign == 1):
            ans += s[index].upper()
            sign = 0
        elif(s[index] == "i" and (s[index - 1] == " " and (s[index + 1] == " " or s[index + 1] == "." or s[index + 1] == "!" or s[index + 1] == "?"))):
            ans += "I"
            sign = 0
        else:
            ans += s[index]
            if(ord(s[index]) >= 65 and ord(s[index]) <= 90):
                sign = 0
            
        index += 1
    
    return ans
    
s = input("Enter line: ")
print(correction(s))