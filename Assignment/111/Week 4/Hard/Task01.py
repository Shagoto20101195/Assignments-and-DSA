s1 = input()
d1 = {}
for x in s1:
    if(x in d1):
        d1[x] = d1.get(x) + 1
    else:
        d1[x] = 1

s2 = input()
d2 = {}
for x in s2:
    if(x in d2):
        d2[x] = d2.get(x) + 1
    else:
        d2[x] = 1

check = True
if(len(d1) == len(d2)):
    for x in d1:
        if(x in d2 and d1.get(x) == d2.get(x)):
            check = False
        else:
            check = True
            break
    
    if(check):
        print("Those strings are not anagrams.")
    else:
        print("Those strings are anagrams.")
            
else:
    print("Those strings are not anagrams.")