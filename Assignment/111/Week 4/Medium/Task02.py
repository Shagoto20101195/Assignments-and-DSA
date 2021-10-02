my_dict = {}
while(True):
    n = input()
    
    if(n == "STOP"):
        break
    else:
        n = int(n)
        
        if(n in my_dict):
            my_dict[n] = my_dict.get(n) + 1
        else:
            my_dict[n] = 1

for i in my_dict:
    print(i, "-", my_dict[i], "times")