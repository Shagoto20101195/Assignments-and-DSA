s1 = input("Enter word: ")
s2 = input("Enter word: ")

ans = ""

for i in s1:
    if(i in s2):
        ans += i
        
for i in s2:
    if(i in s1):
        ans += i
        
if(len(ans) == 0):
    print("Nothing in common.")
else:
    print(ans)