s = input().split(",")
my_dict = {}
for x in s:
    temp = x.split(": ")
    my_dict[temp[0]] = int(temp[1])

while(True):
    n = input()
    
    if(n == "STOP"):
        break
    else:
        n = int(n)
        check = True
        for i in my_dict:
            if(my_dict.get(i) == n):
                check = True
                print(check)
                break
            else:
                check = False
        
        if(not check):
            print(check)